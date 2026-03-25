"""
Helper utilities for the traffic prediction system
"""

import time
import sys
from datetime import datetime

def print_header(text):
    """
    Print a nice formatted header
    """
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60)

def print_slow(text, delay=0.03):
    """
    Print text with a typing effect for better user experience
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def get_valid_input(prompt, valid_options=None, input_type=str):
    """
    Get validated input from user
    """
    while True:
        try:
            user_input = input(prompt)
            
            if valid_options:
                if user_input in valid_options:
                    return user_input
                else:
                    print(f"❌ Invalid choice. Please choose from: {', '.join(valid_options)}")
                    continue
            
            if input_type == int:
                return int(user_input)
            elif input_type == float:
                return float(user_input)
            else:
                return user_input
                
        except ValueError:
            print(f"❌ Invalid input. Please enter a valid {input_type.__name__}.")

def format_time(hour):
    """
    Format hour to AM/PM format
    """
    if hour == 0:
        return "12:00 AM"
    elif hour < 12:
        return f"{hour}:00 AM"
    elif hour == 12:
        return "12:00 PM"
    else:
        return f"{hour-12}:00 PM"

def show_loading_animation(message="Processing", duration=1):
    """
    Show a simple loading animation
    """
    print(message, end="", flush=True)
    for _ in range(duration * 10):
        for char in "|/-\\":
            print(f"\r{message} {char}", end="", flush=True)
            time.sleep(0.05)
    print("\r" + " " * (len(message) + 2), end="", flush=True)
    print("\r", end="", flush=True)

def get_current_day():
    """
    Get current day name
    """
    return datetime.now().strftime("%A")

def get_current_hour():
    """
    Get current hour
    """
    return datetime.now().hour