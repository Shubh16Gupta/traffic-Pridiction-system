import numpy as np
import joblib
import os
import warnings

# Completely suppress all warnings from sklearn
warnings.filterwarnings('ignore')

class TrafficPredictor:
    """
    A class to handle traffic predictions using our trained model
    """
    
    def __init__(self):
        """
        Load the trained model and encoders when creating the predictor
        """
        self.model = None
        self.weather_encoder = None
        self.day_mapping = None
        self.is_loaded = False
        self.feature_names = ['hour', 'day_code', 'weather_code', 'hour_sin', 'hour_cos']
        
        self.load_model()
    
    def load_model(self):
        """
        Load the trained model and encoders from disk
        """
        try:
            model_path = 'models/traffic_model.pkl'
            weather_path = 'models/weather_encoder.pkl'
            day_path = 'models/day_mapping.pkl'
            
            # Check if all files exist
            if not all([os.path.exists(path) for path in [model_path, weather_path, day_path]]):
                print("⚠️  Model files not found!")
                print("   Please run train_model.py first to train the model.")
                return False
            
            # Load the files with warnings suppressed
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                self.model = joblib.load(model_path)
                self.weather_encoder = joblib.load(weather_path)
                self.day_mapping = joblib.load(day_path)
            
            self.is_loaded = True
            print("✅ Model loaded successfully!")
            return True
            
        except Exception as e:
            print(f"❌ Error loading model: {e}")
            return False
    
    def predict_traffic(self, hour, day_of_week, weather):
        """
        Predict traffic for given conditions
        """
        
        if not self.is_loaded:
            return {"error": "Model not loaded. Please check model files."}
        
        # Validate inputs
        if not 0 <= hour <= 23:
            return {"error": f"Hour must be between 0 and 23. Got: {hour}"}
        
        if day_of_week not in self.day_mapping:
            return {"error": f"Invalid day. Choose from: {list(self.day_mapping.keys())}"}
        
        if weather not in self.weather_encoder.classes_:
            return {"error": f"Invalid weather. Choose from: {list(self.weather_encoder.classes_)}"}
        
        # Convert inputs to model format
        day_code = self.day_mapping[day_of_week]
        weather_code = self.weather_encoder.transform([weather])[0]
        
        # Create circular hour features
        hour_sin = np.sin(2 * np.pi * hour / 24)
        hour_cos = np.cos(2 * np.pi * hour / 24)
        
        # Create feature array
        features = np.array([[hour, day_code, weather_code, hour_sin, hour_cos]])
        
        # Make prediction with warnings suppressed
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            traffic_score = self.model.predict(features)[0]
        
        # Determine traffic level
        if traffic_score < 30:
            level = "Low"
            suggestion = "Great time to travel! Roads should be clear."
        elif traffic_score < 65:
            level = "Medium"
            suggestion = "Expect some congestion. Consider checking alternate routes."
        else:
            level = "High"
            suggestion = "Heavy traffic expected! Plan extra time or consider traveling later."
        
        # Get the hour range for peak traffic analysis
        peak_info = self.analyze_peak_hours(day_of_week, weather)
        
        return {
            "traffic_score": round(traffic_score, 1),
            "traffic_level": level,
            "suggestion": suggestion,
            "peak_hours": peak_info
        }
    
    def analyze_peak_hours(self, day_of_week, weather):
        """
        Analyze peak traffic hours for given day and weather
        """
        peak_hours = []
        
        # Check traffic at different hours to find peaks
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            for hour in range(24):
                day_code = self.day_mapping[day_of_week]
                weather_code = self.weather_encoder.transform([weather])[0]
                hour_sin = np.sin(2 * np.pi * hour / 24)
                hour_cos = np.cos(2 * np.pi * hour / 24)
                
                features = np.array([[hour, day_code, weather_code, hour_sin, hour_cos]])
                score = self.model.predict(features)[0]
                
                if score >= 70:  # High traffic threshold
                    peak_hours.append(hour)
        
        if peak_hours:
            # Group consecutive hours
            ranges = []
            start = peak_hours[0]
            end = peak_hours[0]
            
            for hour in peak_hours[1:]:
                if hour == end + 1:
                    end = hour
                else:
                    ranges.append(f"{start}:00-{end+1}:00")
                    start = hour
                    end = hour
            ranges.append(f"{start}:00-{end+1}:00")
            
            return {
                "has_peak": True,
                "hours": ranges,
                "message": f"⚠️  Avoid traveling during: {', '.join(ranges)}"
            }
        else:
            return {
                "has_peak": False,
                "message": "✓ No severe peak hours expected today."
            }

# Create a single instance for use in main program
predictor = TrafficPredictor()