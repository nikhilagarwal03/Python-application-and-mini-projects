"""
 Challenge: Self-Intro Script Generator

Create a Python script that interacts with the user and generates a personalized self-introduction.

Your program should:
1. Ask the user for their name, age, city, profession, and favorite hobby.
2. Format this data into a warm, friendly paragraph of self-introduction.
3. Print the final paragraph in a clean and readable format.

Example:
If the user inputs:
  Name: Priya
  Age: 22
  City: Jaipur
  Profession: Software Developer
  Hobby: playing guitar

Your script might output:
  "Hello! My name is Priya. I'm 22 years old and live in Jaipur. I work as a 
  Software Developer and I absolutely enjoy playing guitar in my free time. 
  Nice to meet you!"

Bonus:
- Add the current date to the end of the paragraph like: "Logged on: 2025-06-14"
- Wrap the printed message with a decorative border of stars (*)
"""

import datetime
import pyttsx3

def announce(message):
  engine = pyttsx3.init()
  # print(message)
  engine.say(message)
  engine.runAndWait()

name = input("What is your name? ").strip()
age = int(input("What is Your Age? ").strip())
city = input("Which City Do you live in? ").strip()
profession = input("What is your profession? ").strip()
hobby = input("What is your Hobby? ").strip()

intro_message = (
  f"Hello! My name is {name}. I'm {age} years old and live in {city}. "
  f"I work as {profession} and I absolutely enjoy {hobby} in my free time. "
  f"Nice to meet you!\n"
)

current_date = datetime.datetime.now().strftime("%d-%m-%Y")
current_time = datetime.datetime.now().strftime("%H:%M:%S")
updated_intro_message = f"{intro_message} \n Generated on: {current_date} and Time: {current_time} "

border = ("\n" + "*" *100)
final_output = f"\n{border}\n{updated_intro_message}\n{border}"
print(final_output)
announce(intro_message)
