"""
 Challenge: Minutes Alive Calculator

Write a Python script that calculates approximately how many minutes old a person is,
based on their age in years.

Your program should:
1. Ask the user for their age in years (accept float values too).
2. Convert that age into:
   - Total days
   - Total hours
   - Total minutes
3. Display the result in a readable format.

Assumptions:
- You can use 365.25 days/year to account for leap years.
- You don't need to handle time zones or exact birthdates in this version.

Example:
Input:
  Age: 25

Output:
  You are approximately:
    - 9,131 days old
    - 219,144 hours old
    - 13,148,640 minutes old

Bonus:
- Add comma formatting for large numbers
- Let the user try again without restarting the program
"""
def function(age_years):
    DAYS_IN_YEAR = 365.25
    HOURS_IN_DAY = 24
    MINUTES_IN_HOUR = 60

    total_days = age_years * DAYS_IN_YEAR
    total_hours = total_days * HOURS_IN_DAY
    total_minutes = total_hours * MINUTES_IN_HOUR

    return round(total_days), round(total_hours), round(total_minutes)

while True:
    try:
        age = float(input("Enter Your Age(in Years): "))
        days, hours, minutes = function(age)

        print(f"""\n You are approximately: 
              - {days} days old
              - {hours} hours old
              - {minutes} minutes old\n
        """)
        
        again = input("would you like to try again? (y/n): ")

        if again != "y":
            print("thanks for using the python script")
            break
    except:
        print("please enter valid age (in years)")