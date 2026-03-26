import time
import sys
from datetime import datetime
"""Print headder"""
def header_priting(text):
    '''this will print the header line in a good and nice way'''
    print("\n" + "=" * 60)
    '''take the text and print it'''
    print(f"  {text}")
    print("=" * 60)
    '''end the header with the same ending line'''

"""typing effect text"""
def slow_printing(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        '''this make the output instatly'''
        sys.stdout.flush()
        '''delay the text'''
        time.sleep(delay)
    print()

"""input validity"""
def check_input(prompt, valid_options=None, input_type=str):
    while True:
        try:
            '''takes the user input'''
            user_input = input(prompt)
            '''check whether the input is correct or not by simple of else'''
            if valid_options:
                if user_input in valid_options:
                    return user_input
                else:
                    print(f"Invalid choice. Please choose from: {', '.join(valid_options)}")
                    continue
            '''print the conditions'''
            if input_type == int:
                return int(user_input)
            elif input_type == float:
                return float(user_input)
            else:
                return user_input    
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")
'''use to convet the time by simple conditional statement'''
def time_convert(hour):
    if hour == 0:
        return "12:00 AM"
    elif hour < 12:
        return f"{hour}:00 AM"
    elif hour == 12:
        return "12:00 PM"
    else:
        return f"{hour-12}:00 PM"
'''this will give the loding animations'''
def loding_animation(message="Processing", duration=1):
    print(message, end="", flush=True)
    for _ in range(duration * 10):
        for char in "|/-\\":
            print(f"\r{message} {char}", end="", flush=True)
            time.sleep(0.05)
    print("\r" + " " * (len(message) + 2), end="", flush=True)
    print("\r", end="", flush=True)
'''fetch the day and hour'''
def get_day():
    return datetime.now().strftime("%A")
def get_hour():
    return datetime.now().hour