"""
Challenge: Password Strength Checker & Suggestion Tool

Build a Python script that checks the strength of a password based on:
1. Length (at least 8 characters)
2. At least one uppercase letter
3. At least one lowercase letter
4. At least one digit
5. At least one special character (e.g., @, #, $, etc.)

Your program should:
- Ask the user to input a password.
- Tell them what's missing if it's weak.
- If the password is strong, confirm it.
- Suggest a strong random password if the input is weak.

Bonus:
- Hide password input using `getpass` (no echo on screen).
"""

import string
import random
import getpass
import pyttsx3

def announce(message):
    engine = pyttsx3.init()
    print(message)
    engine.say(message)
    engine.runAndWait()

def check_password_strength(password):
    issues = []
    if len(password) < 8 :
        issues.append("Password Should be Atleast 8 Characters long.")
    if not any(c.islower() for c in password):
        issues.append("Password should contain Atleast one Lowercase letter")
    if not any(c.isupper() for c in password):
        issues.append("Password should contain Atleast one Uppercase letter")
    if not any(c.isdigit() for c in password):
        issues.append("Password should contain Atleast one Digit")
    if not any(c in string.punctuation for c in password):
        issues.append("Password should contain Atleast one special character (e.g., @, #, $, etc.)")
    return issues

def generate_Strong_password(length = 12):
    chars = string.ascii_letters + string.digits + string.punctuation

    return "".join(random.choice(chars) for _ in range(length))

password = getpass.getpass("Enter a Password: ")
issues = check_password_strength(password)

if not issues:
    announce("That's a Strong Password.")
else:
    announce("That's a weak Password.")
    for issue in issues:
        announce(f"- {issue}")

suggestion = generate_Strong_password()
announce("\n suggesting you a strong password")
print(suggestion)