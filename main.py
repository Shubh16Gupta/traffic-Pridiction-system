#!/usr/bin/env python3
"""
Smart Urban Traffic Prediction System - Console Version
A machine learning-based traffic prediction system for smarter travel planning
"""

# Suppress all warnings for cleaner output
import warnings
warnings.filterwarnings('ignore')

import sys
import os
from datetime import datetime

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.predict import predictor
from src.utils import (
    header_priting, slow_printing, check_input, 
    time_convert, loding_animation, get_day, get_hour
)

def show_welcome():
    """
    Display welcome message and system info
    """
    header_priting("🚦 SMART URBAN TRAFFIC PREDICTION SYSTEM")
    slow_printing("\n🌆 Welcome to the Intelligent Traffic Prediction System!")
    slow_printing("   This system uses machine learning to help you avoid traffic congestion.")
    slow_printing("   Based on time, day, and weather conditions, we'll predict traffic intensity.")
    slow_printing("   Make smarter travel decisions and save time on the road! 🚗💨\n")
    
    # Show current conditions if model is loaded
    if predictor.is_loaded:
        current_day = get_day()
        current_hour = get_hour()
        current_weather = "Clear"  # You could integrate real weather API here
        
        print("📍 Current Conditions:")
        print(f"   📅 Day: {current_day}")
        print(f"   ⏰ Time: {time_convert(current_hour)}")
        print(f"   ☁️  Weather: {current_weather} (default)")
        
        # Show current traffic prediction
        print("\n🔍 Predicting current traffic conditions...")
        loding_animation("Analyzing patterns", 1)
        
        current_pred = predictor.predict_traffic(current_hour, current_day, current_weather)
        if "error" not in current_pred:
            print(f"\n📊 Current Traffic: {current_pred['traffic_level']} Level")
            print(f"   Traffic Score: {current_pred['traffic_score']}/100")
            print(f"   💡 {current_pred['suggestion']}")
    
    input("\nPress Enter to continue...")

def main_menu():
    """
    Display main menu and handle user choice
    """
    while True:
        header_priting("📋 MAIN MENU")
        print("1. 🔮 Predict Traffic for a Specific Time")
        print("2. 🔄 What-If Analysis (Compare Different Times)")
        print("3. ⏰ Find Best Time to Travel")
        print("4. 📈 Peak Hours Intelligence")
        print("5. ℹ️  About This System")
        print("6. 🚪 Exit")
        
        choice = check_input("\n👉 Enter your choice (1-6): ", 
                                 valid_options=['1', '2', '3', '4', '5', '6'])
        
        if choice == '1':
            predict_traffic()
        elif choice == '2':
            what_if_analysis()
        elif choice == '3':
            find_best_time()
        elif choice == '4':
            peak_hours_intelligence()
        elif choice == '5':
            show_about()
        elif choice == '6':
            slow_printing("\n👋 Thank you for using Smart Traffic Prediction System!")
            slow_printing("   Drive safe and plan smart! 🚗✨\n")
            sys.exit(0)

def predict_traffic():
    """
    Get user input and show traffic prediction
    """
    header_priting("🔮 TRAFFIC PREDICTION")
    
    # Get user inputs
    print("\n📝 Please provide the following information:")
    
    # Day selection
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print("\n📅 Days of week:")
    for i, day in enumerate(days, 1):
        print(f"   {i}. {day}")
    
    day_choice = check_input("Select day (1-7): ", valid_options=[str(i) for i in range(1, 8)])
    day = days[int(day_choice) - 1]
    
    # Hour selection
    print("\n⏰ Travel time:")
    print("   (Use 24-hour format, 0-23)")
    print("   💡 Rush hours: 8-10 AM and 5-7 PM")
    hour = check_input("Enter hour (0-23): ", input_type=int)
    while hour < 0 or hour > 23:
        print("❌ Hour must be between 0 and 23")
        hour = check_input("Enter hour (0-23): ", input_type=int)
    
    # Weather selection
    weathers = ['Clear', 'Cloudy', 'Rain', 'Fog', 'Snow']
    print("\n☁️  Weather conditions:")
    for i, weather in enumerate(weathers, 1):
        print(f"   {i}. {weather}")
    
    weather_choice = check_input("Select weather (1-5): ", valid_options=[str(i) for i in range(1, 6)])
    weather = weathers[int(weather_choice) - 1]
    
    # Show prediction
    print("\n🔄 Analyzing traffic patterns...")
    loding_animation("Calculating prediction", 1)
    
    result = predictor.predict_traffic(hour, day, weather)
    
    if "error" in result:
        print(f"\n❌ Error: {result['error']}")
        return
    
    # Display results
    header_priting("📊 PREDICTION RESULTS")
    print(f"\n🎯 Travel Time: {time_convert(hour)} on {day}")
    print(f"🌤️  Weather: {weather}")
    print(f"\n🚦 Traffic Score: {result['traffic_score']}/100")
    print(f"📈 Traffic Level: {result['traffic_level']}")
    
    # Color-coded visual indicator
    if result['traffic_level'] == "Low":
        print("   [🟢-----------] (Light traffic expected)")
    elif result['traffic_level'] == "Medium":
        print("   [🟡🟡--------] (Moderate traffic expected)")
    else:
        print("   [🔴🔴🔴🔴🔴---] (Heavy traffic expected)")
    
    print(f"\n💡 Recommendation: {result['suggestion']}")
    
    # Show peak hours if relevant
    if result['peak_hours']['has_peak']:
        print(f"\n⚠️  Peak Hours Alert: {result['peak_hours']['message']}")
    
    input("\n\nPress Enter to return to main menu...")

def what_if_analysis():
    """
    Compare traffic at different times
    """
    header_priting("🔄 WHAT-IF ANALYSIS")
    print("\nLet's compare traffic at different times to find the best option!")
    
    # First scenario
    print("\n📌 Scenario 1:")
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print("\nDays of week:")
    for i, day in enumerate(days, 1):
        print(f"   {i}. {day}")
    
    day1_choice = check_input("Select day (1-7): ", valid_options=[str(i) for i in range(1, 8)])
    day1 = days[int(day1_choice) - 1]
    
    hour1 = check_input("Enter travel hour (0-23): ", input_type=int)
    
    weathers = ['Clear', 'Cloudy', 'Rain', 'Fog', 'Snow']
    print("\nWeather conditions:")
    for i, weather in enumerate(weathers, 1):
        print(f"   {i}. {weather}")
    
    weather1_choice = check_input("Select weather (1-5): ", valid_options=[str(i) for i in range(1, 6)])
    weather1 = weathers[int(weather1_choice) - 1]
    
    # Second scenario
    print("\n📌 Scenario 2:")
    print("\nWould you like to:")
    print("1. Compare with a different hour on the same day")
    print("2. Compare with a completely different scenario")
    
    compare_choice = check_input("Choose (1-2): ", valid_options=['1', '2'])
    
    if compare_choice == '1':
        hour2 = check_input("Enter alternative hour (0-23): ", input_type=int)
        day2 = day1
        weather2 = weather1
    else:
        print("\nSelect day for second scenario:")
        day2_choice = check_input("Select day (1-7): ", valid_options=[str(i) for i in range(1, 8)])
        day2 = days[int(day2_choice) - 1]
        
        hour2 = check_input("Enter travel hour (0-23): ", input_type=int)
        
        print("\nSelect weather for second scenario:")
        weather2_choice = check_input("Select weather (1-5): ", valid_options=[str(i) for i in range(1, 6)])
        weather2 = weathers[int(weather2_choice) - 1]
    
    # Perform analysis
    print("\n🔄 Comparing scenarios...")
    loding_animation("Analyzing both scenarios", 1)
    
    # Get predictions for both scenarios
    result1 = predictor.predict_traffic(hour1, day1, weather1)
    result2 = predictor.predict_traffic(hour2, day2, weather2)
    
    if "error" in result1 or "error" in result2:
        print("\n❌ Error in prediction. Please check your inputs.")
        return
    
    # Display comparison
    header_priting("📊 COMPARISON RESULTS")
    
    print("\n🎯 SCENARIO 1:")
    print(f"   Time: {time_convert(hour1)} on {day1}")
    print(f"   Weather: {weather1}")
    print(f"   Traffic Score: {result1['traffic_score']}/100")
    print(f"   Level: {result1['traffic_level']}")
    
    print("\n🎯 SCENARIO 2:")
    print(f"   Time: {time_convert(hour2)} on {day2}")
    print(f"   Weather: {weather2}")
    print(f"   Traffic Score: {result2['traffic_score']}/100")
    print(f"   Level: {result2['traffic_level']}")
    
    # Determine which is better
    print("\n💡 ANALYSIS:")
    if result1['traffic_score'] < result2['traffic_score']:
        difference = result2['traffic_score'] - result1['traffic_score']
        print(f"   ✅ Scenario 1 is better by {difference:.1f} points!")
        print(f"   👉 {result1['suggestion']}")
    elif result2['traffic_score'] < result1['traffic_score']:
        difference = result1['traffic_score'] - result2['traffic_score']
        print(f"   ✅ Scenario 2 is better by {difference:.1f} points!")
        print(f"   👉 {result2['suggestion']}")
    else:
        print("   🤔 Both scenarios have similar traffic conditions.")
    
    input("\n\nPress Enter to return to main menu...")

def find_best_time():
    """
    Find the best time to travel on a given day
    """
    header_priting("⏰ FIND BEST TRAVEL TIME")
    
    print("\nI'll help you find the best time to travel on a specific day!")
    
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print("\nSelect day:")
    for i, day in enumerate(days, 1):
        print(f"   {i}. {day}")
    
    day_choice = check_input("Select day (1-7): ", valid_options=[str(i) for i in range(1, 8)])
    day = days[int(day_choice) - 1]
    
    weathers = ['Clear', 'Cloudy', 'Rain', 'Fog', 'Snow']
    print("\nExpected weather:")
    for i, weather in enumerate(weathers, 1):
        print(f"   {i}. {weather}")
    
    weather_choice = check_input("Select weather (1-5): ", valid_options=[str(i) for i in range(1, 6)])
    weather = weathers[int(weather_choice) - 1]
    
    print("\n🔍 Analyzing all hours of the day...")
    loding_animation("Finding optimal travel times", 2)
    
    # Check all hours
    best_hour = None
    best_score = 100
    predictions = []
    
    for hour in range(24):
        result = predictor.predict_traffic(hour, day, weather)
        if "error" not in result:
            predictions.append((hour, result['traffic_score']))
            if result['traffic_score'] < best_score:
                best_score = result['traffic_score']
                best_hour = hour
    
    # Display results
    header_priting(f"📊 BEST TIMES FOR {day}")
    
    print(f"\n🌤️  Weather: {weather}")
    print(f"\n🌟 BEST TIME: {time_convert(best_hour)}")
    
    best_result = predictor.predict_traffic(best_hour, day, weather)
    print(f"   Traffic Score: {best_result['traffic_score']}/100")
    print(f"   Level: {best_result['traffic_level']}")
    print(f"\n💡 {best_result['suggestion']}")
    
    # Show top 3 best times
    sorted_times = sorted(predictions, key=lambda x: x[1])[:3]
    print(f"\n📅 Top 3 Best Travel Times:")
    for hour, score in sorted_times:
        result = predictor.predict_traffic(hour, day, weather)
        print(f"   {time_convert(hour)}: {score:.0f}/100 ({result['traffic_level']})")
    
    # Show worst times to avoid
    sorted_times = sorted(predictions, key=lambda x: x[1], reverse=True)[:3]
    print(f"\n⚠️  Times to Avoid:")
    for hour, score in sorted_times:
        print(f"   {time_convert(hour)}: {score:.0f}/100 (Heavy traffic expected)")
    
    input("\n\nPress Enter to return to main menu...")

def peak_hours_intelligence():
    """
    Show peak hours intelligence information
    """
    header_priting("📈 PEAK HOURS INTELLIGENCE")
    
    print("\n🎯 Peak Hours Intelligence helps you avoid rush hour congestion!")
    print("\nLet me analyze peak traffic hours for your preferred travel day.\n")
    
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print("Select day to analyze:")
    for i, day in enumerate(days, 1):
        print(f"   {i}. {day}")
    
    day_choice = check_input("\nSelect day (1-7): ", valid_options=[str(i) for i in range(1, 8)])
    day = days[int(day_choice) - 1]
    
    weathers = ['Clear', 'Cloudy', 'Rain', 'Fog', 'Snow']
    print("\nWeather condition:")
    for i, weather in enumerate(weathers, 1):
        print(f"   {i}. {weather}")
    
    weather_choice = check_input("Select weather (1-5): ", valid_options=[str(i) for i in range(1, 6)])
    weather = weathers[int(weather_choice) - 1]
    
    print(f"\n🔍 Analyzing peak traffic for {day}...")
    loding_animation("Scanning traffic patterns", 2)
    
    result = predictor.predict_traffic(12, day, weather)  # Just to get peak info
    if "error" in result:
        print(f"\n❌ Error: {result['error']}")
        return
    
    header_priting(f"📊 PEAK HOURS ANALYSIS FOR {day}")
    
    if result['peak_hours']['has_peak']:
        print(f"\n⚠️  {result['peak_hours']['message']}")
        print("\n💡 Smart Recommendation:")
        print("   Avoid traveling during these peak hours to save time!")
        
        # Find the best alternative
        best_hour = None
        best_score = 100
        
        for hour in range(24):
            if hour in [int(h.split(':')[0]) for h in result['peak_hours']['hours']]:
                continue
            pred = predictor.predict_traffic(hour, day, weather)
            if pred['traffic_score'] < best_score:
                best_score = pred['traffic_score']
                best_hour = hour
        
        if best_hour is not None:
            print(f"\n✅ Recommended alternative: {time_convert(best_hour)}")
            print(f"   Expected traffic: {best_score:.0f}/100")
    else:
        print(f"\n✅ Good news! No severe peak hours on {day} with {weather} weather.")
        print("   You have flexibility in choosing your travel time.")
    
    input("\n\nPress Enter to return to main menu...")

def show_about():
    """
    Display information about the system
    """
    header_priting("ℹ️  ABOUT THE SYSTEM")
    
    print("""
🌟 SMART URBAN TRAFFIC PREDICTION SYSTEM
=========================================

🎯 Mission:
Help urban commuters make smarter travel decisions by predicting 
traffic conditions before they hit the road.

🤖 How It Works:
- Uses Random Forest machine learning algorithm
- Trained on 10,000+ synthetic traffic scenarios
- Considers time of day, day of week, and weather conditions
- Provides traffic scores and actionable recommendations

✨ Key Features:
1. Real-time traffic prediction
2. What-if scenario analysis  
3. Peak hours intelligence
4. Best travel time recommendations
5. User-friendly console interface

📊 Prediction Categories:
- Low Traffic (0-30): Smooth sailing! 🟢
- Medium Traffic (30-65): Some delays expected 🟡
- High Traffic (65-100): Heavy congestion 🔴

Future Enhancements:
 Real-time GPS integration
-Live weather API connection
-Mobile app version
-Deep learning models for better accuracy
-Traffic heatmap visualization

Pro Tip:
Use the What-If Analysis to compare different travel times 
and find the perfect window for your journey!

---
Made with 🚗💨 for smarter cities and happier commuters
    """)   
    input("\nPress Enter to return to main menu...")
if __name__ == "__main__":
    try:
        show_welcome()
        main_menu()
    except KeyboardInterrupt:
        print("\n\n👋 Thanks for using Smart Traffic Prediction System!")
        print("   Drive safe! 🚗✨")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
        print("   Please restart the application.")
        sys.exit(1)