"""
 Challenge: Friendship Compatibility Calculator

Build a Python script that calculates a fun "compatibility score" between two friends based on their names.

Your program should:
1. Ask for two names (friend A and friend B).
2. Count shared letters, vowels, and character positions to create a compatibility
score (0-100).
3. Display the percentage with a themed message like:
   "You're like chai and samosa — made for each other!" or 
   "Well... opposites attract, maybe?"

Bonus:
- Use emojis in the result
- Give playful advice based on the score range
- Capitalize and center the final output in a framed box
"""
import random

def freindship_score(name1, name2):
    name1, name2 = name1.lower(), name2.lower()
    score = 10 
    common_letters = set(name1) & set(name2)
    vowels = set('aeiou')

    score += len(common_letters) * 5
    score += len(vowels & common_letters) * 10
    
    return min(score, 100)

def run_function():
    name1 = input("Enter first name: ")
    name2 = input("Enter second name: ")
    
    score = freindship_score(name1,name2)

    print(f"\n {score}")
    
    def themed_message(score):
        high = [
            "You're like chai and samosa — made for each other!",
            "Dynamic duo! You two are inseparable!",
            "Best friends forever vibes!"
        ]
        medium = [
            "You both are like chai and coffee. Different, unique but still similar.", 
            "A solid friendship in progress!",
            "Some sparks here and there, keep building!"
        ]
        low_medium = [
            "Well... opposites attract, maybe?",
            "Your friendship is like a slow-cooked dish, takes time to perfect.",
            "Different strokes, still okay together."
        ]
        low = [
            "Low Score!! No Comments.",
            "Maybe not meant to be BFFs 😅",
            "Could use some bonding time!"
        ]
        
        if score > 80:
            print(random.choice(high))
        elif 50 < score <= 80:
            print(random.choice(medium))
        elif 20 < score <= 50:
            print(random.choice(low_medium))
        else:
            print(random.choice(low))
    
    themed_message(score)

run_function()