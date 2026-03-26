"""
This script trains our Random Forest model to predict traffic conditions.
It takes the historical traffic data and learns patterns to make predictions.
"""
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import os
def prepare_data(df):
    print("🔄 Preparing data for training...")   
    # Create a copy to avoid modifying original
    data = df.copy()   
    # Convert day of week to numbers (Monday=0, Sunday=6)
    day_mapping = {
        'Monday': 0, 'Tuesday': 1, 'Wednesday': 2,
        'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6
    }
    data['day_code'] = data['day_of_week'].map(day_mapping)    
    # Encode weather conditions
    weather_encoder = LabelEncoder()
    data['weather_code'] = weather_encoder.fit_transform(data['weather'])    
    # Create a feature to represent time of day in a circular way
    # This helps the model understand that 23:00 and 00:00 are close
    data['hour_sin'] = np.sin(2 * np.pi * data['hour'] / 24)
    data['hour_cos'] = np.cos(2 * np.pi * data['hour'] / 24)  
    # Select features for training
    features = ['hour', 'day_code', 'weather_code', 'hour_sin', 'hour_cos']
    target = 'traffic_score'
    
    X = data[features]
    y = data[target]
    
    print(f"✅ Features prepared: {features}")
    print(f"   Total samples: {len(X)}")    
    return X, y, weather_encoder, day_mapping

def train_and_save_model():   
    print("🚦 Starting Traffic Prediction Model Training")
    print("=" * 50)   
    # Check if data exists
    data_path = 'data/traffic_data.csv'
    if not os.path.exists(data_path):
        print("❌ No training data found!")
        print("   Please run data_generator.py first to create the dataset.")
        return None   
    # Load the data
    print(f"📂 Loading data from {data_path}...")
    df = pd.read_csv(data_path)
    print(f"   Loaded {len(df)} records")   
    # Prepare data
    X, y, weather_encoder, day_mapping = prepare_data(df)   
    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )  
    print(f"\n📊 Training set: {len(X_train)} samples")
    print(f"📊 Testing set: {len(X_test)} samples")  
    # Create and train the Random Forest model
    print("\n🤖 Training Random Forest model...")
    model = RandomForestRegressor(
        n_estimators=100,      # tree number quantity
        max_depth=15,          # Maximum depth of each tree
        min_samples_split=10,  # Minimum samples to split a node
        min_samples_leaf=5,    # Minimum samples in a leaf node
        random_state=42,
        n_jobs=-1              # it will use all the core of the cpu
    ) 
    model.fit(X_train, y_train)
    print("✅ Model training complete!")   
    # Evaluate the model and tell the performance of the model
    print("\n📈 Model Performance:")
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"   Mean Absolute Error: {mae:.2f} points")
    print(f"   R² Score: {r2:.3f}")
    print(f"   Accuracy (within ±10 points): {(abs(y_test - y_pred) <= 10).mean()*100:.1f}%")
    
    # Save the model and and do for the later peroformance
    print("\n💾Saving model and encoders")  
    # Create models directory if it doesn't exist
    os.makedirs('models', exist_ok=True)
    
    # Save the model
    joblib.dump(model, 'models/traffic_model.pkl') 
    # Save the encoders for later use
    joblib.dump(weather_encoder, 'models/weather_encoder.pkl')
    joblib.dump(day_mapping, 'models/day_mapping.pkl')
    
    print("✅ Model saved to 'models/traffic_model.pkl'")
    print("✅ Encoders saved to 'models/weather_encoder.pkl'")
    return model, weather_encoder, day_mapping
if __name__ == "__main__":
    train_and_save_model()