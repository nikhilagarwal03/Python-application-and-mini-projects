"""
Challenge: Stylish Bio Generator for Instagram/Twitter

Create a Python utility that asks the user for a few key details and generates a short, stylish bio that could be used for social media profiles like Instagram or Twitter.

Your program should:
1. Prompt the user to enter their:
   - Name
   - Profession
   - One-liner passion or goal
   - Favorite emoji (optional)
   - Website or handle (optional)

2. Generate a stylish 2-3 line bio using the inputs. It should feel modern, concise, and catchy.

3. Add optional hashtags or emojis for flair.

Example:
Input:
  Name: Riya
  Profession: Designer
  Passion: Making things beautiful
  Emoji: 🎨
  Website: @riya.design

Output:
  🎨 Riya | Designer  
  💡 Making things beautiful  
  🔗 @riya.design

Bonus:
- Let the user pick from 2-3 different layout styles.
- Ask the user if they want to save the result into a `.txt` file.
"""
import textwrap
name = input("Enter Your Name: ").strip()
profession = input("Enter Your profession: ").strip()
passion = input("Enter Your passion in one line: ").strip()
emoji = input("Enter Your fav emoji: ").strip()
website = input("Enter Your website/handle: ").strip()

print("\nChoose your Style: ")
print("1. Simple lines")
print("2. Vertical flair")
print("3. Emoji sandwich")

style = input("enter 1,2, or 3: ").strip()

def generate_bio(style, name, profession, passion, emoji, website):
    if style == "1":
        return f"""{name} | {profession}
Passionate about {passion}
Connect: {website} {emoji}"""
    elif style == "2":
        return f"""{name}
{profession}
{passion}
{emoji}
{website}"""
    elif style == "3":
        return f"""{emoji} {emoji} {emoji}
{name} — {profession}
Loves {passion}
Find me at: {website}
{emoji} {emoji} {emoji}"""
    else:
        return "Invalid choice! Please restart and pick 1, 2, or 3."
    
bio = generate_bio(style, name, profession, passion, emoji, website)

print("\nYour Stylish Bio: ")
print("\n" + "*" *100)
print(textwrap.dedent(bio))
print("\n" + "*" *100)

save = input("Would you like to get generated bio as a txt file (y/n)? ").lower()

if save == "y":
    filename = f"{name.lower().replace(' ','_')}.bio.txt"
    with open(filename,"w",encoding="utf-8") as f:
        f.write(bio)
    print(f"File Saved as {filename}")
