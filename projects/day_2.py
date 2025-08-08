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

name = input("Enter your name : ").strip()
profession = input("Enter your profession : ").strip()
passion = input("Enter your passion : ").strip()
emoji = input("Enter your emoji : ").strip()
website = input("Enter your website : ").strip()

print("\nChoose your style : ")
print("\n1. Simple style")
print("\n2. Vertical style")
print("\n3. Emoji style")

style = input("Enter 1, 2 or 3 : ").strip()

def generate_bio(style):
    if style == "1":
        return f"{emoji} || {name} \n{emoji} || {profession} \n{emoji} || {passion} \n{emoji} || {website}"
    elif style == "2":
        return f"--> {name} | {profession} <-- \n--> {passion} | {website} <--\n {emoji*5}"
    elif style == "3":
        return f"{emoji*3} - {name}\n{emoji*3} - {profession}\n{emoji*3} - {passion}\n{emoji*3} - {website}"
    else:
        return "Invalid style selected."

bio = generate_bio(style)

print("\n *** Your stylish bio *** ")
print('*' * 50)
print(textwrap.dedent(bio))
print('*' * 50)

save = input("Do you want to save this bio to a text file? (yes/no) : ").lower()

if save == 'yes':
    filename = f"{name.lower().replace(' ','_')}_bio.txt"
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(bio)
    print("File saved!!!")
else: 
    print("Visit us later!")