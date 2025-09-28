"""
Challenge: Set a Countdown Timer

Create a Python script that allows the user to set a timer in seconds. The script should:

1. Ask the user for the number of seconds to set the timer.
2. Show a live countdown in the terminal.
3. Notify the user when the timer ends with a final message and sound (if possible).

Bonus:
- Format the remaining time as MM:SS
- Use a beep sound (`\a`) at the end if the terminal supports it
- Prevent negative or non-integer inputs
"""

import time
import winsound
import pyttsx3

def announce(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

while True:
    try:
        seconds = int(input("Enter the time in seconds: "))
        if seconds < 1:
            print("Enter the time seconds greater than 0")
            continue
        break
    except ValueError:
        print("Invalid Input Type, enter only whole numbers")

print("Starting Timer...")
for remaining in range(seconds,0,-1):
    mins, secs = divmod(remaining,60)
    time_format = f"{mins:02}:{secs:02}"
    # print(f"Time Left: {time_format}" , end="\n") # prints on every next line
    print(f"Time Left: {time_format}" , end="\r") # prints on very same line 
    time.sleep(1)

print("Timer Completed... ")
winsound.Beep(1000 , 1000)
announce("Timer completed")