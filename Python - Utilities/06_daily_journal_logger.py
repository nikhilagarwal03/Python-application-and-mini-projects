"""
Challenge: Daily Learning Journal Logger

Build a Python script that allows you to maintain a daily learning journal. Each entry will be saved into a `.txt` file along with a timestamp.

Your program should:
1. Ask the user what they learned today.
2. Add the entry to a file called `learning_journal.txt`.
3. Each entry should include the date and time it was written.
4. The journal should **append** new entries rather than overwrite.

Bonus:
- Add an optional rating (1-5) for how productive the day was.
- Show a confirmation message after saving the entry.
- Make sure the format is clean and easy to read when opening the file.

Example:
📅 2025-06-14 — 10:45 AM
Today I learned about how list comprehensions work in Python!
Productivity Rating: 4/5
"""
import datetime
import os
import pyttsx3

def announce(message):
    engine = pyttsx3.init()
    print(message)
    engine.say(message)
    engine.runAndWait()

learning = input("What did you learn Today? ").strip()
rating = input("⭐️ rate your productivity today (1-5, optional): ").strip()

current_date = datetime.datetime.now().strftime("%d/%m/%Y")
current_time = datetime.datetime.now().strftime("%H:%M:%S")

journal_entry = f"\n 🗓️{current_date} , {current_time}\n {learning}"
if rating:
    journal_entry += f"\n Productivity Rating: {rating}/5 \n"
FILE_NAME = "learning_journal.txt"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TASK_FILE = os.path.join(BASE_DIR, FILE_NAME)

with open(TASK_FILE,"a",encoding="utf-8") as f:
    f.write(journal_entry)

announce(f"\n your journal entry has been saved to {FILE_NAME} file. ")
