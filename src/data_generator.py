"""
This script creates synthetic traffic data for training our prediction model.
The data simulates real-world patterns where traffic varies based on:
- Time of day (morning rush, afternoon, evening rush, night)
- Day of week (weekdays busier than weekends)
- Weather conditions (rain/snow increase congestion)
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
def generate_traffic_data(num_records=10000):
    """
    Generate synthetic traffic data with realistic patterns 
    Parameters:
    num_records: Number of data records to generate
    
    Returns:
    DataFrame with traffic data
    """  
    print(f"🌱 Generating {num_records} synthetic traffic records...")    
    # Define our possible values
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weathers = ['Clear', 'Cloudy', 'Rain', 'Fog', 'Snow']  
    # Base traffic intensity by hour (higher means more traffic)
    # This is the "typical" pattern without weather influence
    hour_pattern = {
        0: 15, 1: 10, 2: 8, 3: 5, 4: 8, 5: 20,    # Early morning
        6: 35, 7: 55, 8: 65, 9: 50,                # Morning rush
        10: 40, 11: 45, 12: 55, 13: 60,            # Midday
        14: 55, 15: 50, 16: 65, 17: 80,            # Evening rush starts
        18: 75, 19: 60, 20: 45, 21: 35,            # Evening
        22: 25, 23: 20                             # Night
    }   
    # Day modifiers (weekdays are busier than weekends)
    day_modifier = {
        'Monday': 1.2,
        'Tuesday': 1.2,
        'Wednesday': 1.2,
        'Thursday': 1.2,
        'Friday': 1.3,      # Friday is extra busy
        'Saturday': 0.8,    # Weekend - less traffic
        'Sunday': 0.7       # Sunday - quietest
    }   
   # Weather modifiers (bad weather increases traffic congestion)
    weather_modifier = {
        'Clear': 1.0,
        'Cloudy': 1.1,
        'Rain': 1.4,
        'Fog': 1.3,
        'Snow': 1.6
    }    
    data = []    
    for _ in range(num_records):
        # Randomly select day, hour, and weather
        day = random.choice(days)
        hour = random.randint(0, 23)
        weather = random.choice(weathers)      
        # Calculate base traffic from hour pattern
        base_traffic = hour_pattern[hour]       
        # Apply modifiers
        day_factor = day_modifier[day]
        weather_factor = weather_modifier[weather]        
        # Calculate final traffic intensity
        # Add some randomness to make it realistic (±10%)
        random_factor = random.uniform(0.9, 1.1)        
        traffic_score = base_traffic * day_factor * weather_factor * random_factor       
        # Ensure score stays within 0-100 range
        traffic_score = max(0, min(100, traffic_score))       
        # Determine traffic level based on score
        if traffic_score < 30:
            level = "Low"
        elif traffic_score < 65:
            level = "Medium"
        else:
            level = "High"      
        data.append({
            'hour': hour,
            'day_of_week': day,
            'weather': weather,
            'traffic_score': round(traffic_score, 2),
            'traffic_level': level
        })   
    # Create DataFrame
    df = pd.DataFrame(data)    
    print(f"✅ Generated {len(df)} records successfully!")
    print(f"\n📊 Quick preview of the data:")
    print(df.head(10))
    print(f"\n📈 Traffic level distribution:")
    print(df['traffic_level'].value_counts())
    
    return df
if __name__ == "__main__":
    # Test the generator
    df = generate_traffic_data(5000)
    df.to_csv('data/traffic_data.csv', index=False)
    print("\n💾 Data saved to 'data/traffic_data.csv'")