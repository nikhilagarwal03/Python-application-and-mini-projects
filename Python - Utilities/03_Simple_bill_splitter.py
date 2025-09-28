"""
 Challenge: Simple Bill Splitter

Write a Python script that helps split a bill evenly between friends.

Your program should:
1. Ask how many people are in the group.
2. Ask for each person's name.
3. Ask for the total bill amount.
4. Calculate each person's share of the bill.
5. Display how much each person owes in a clean, readable format.

Example:
Total bill: ₹1200  
People: Aman, Neha, Ravi

Each person owes: ₹400

Final output:
  Aman owes ₹400  
  Neha owes ₹400  
  Ravi owes ₹400

Bonus:
- Round to 2 decimal places
- Print a decorative summary box
"""
import pyttsx3

def announce(message):
    engine = pyttsx3.init()
    print(message)
    engine.say(message)
    engine.runAndWait()

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please Enter a valid number")

num_people = int(input("how many people are there in the group: "))
names = []

for i in range(num_people):
    name = input(f"Enter the name of person {i+1}: ").strip()
    names.append(name)

total_bill = get_float("Enter the Total bill Amount: ")

share = round(total_bill/num_people,2)

print("\n" + "*" *100)
announce(f"Total Bill is: {total_bill}")
announce(f"Each person owes {share}")
for name in names:
    announce(f"{name} owes ₹{share}")
print("\n" + "*" *100)