"""
Challenge : Self-Intro Script Generator

Create a python script that interacts with the user and generated with the user and generates a personalized self-introduction.

Your program should:
1. Ask the user for their name, age, city, profession, and favorite hobby.
2. Format this data into a warm, fridenly paragraph of self-introduction.
3. Print the final paragraph in a clean and readable format.

Example:
If the user inputs:
    Name: Priya
    Age: 22
    City: Jaipur
    Profession: Software Developer
    Hobby: Playing guitar

Your script might output:
    "Hello! My name is Priya. I'm 22 years old and live in Jaipur. I work as a Software Developer and I absolutely enjoy playing guitar in my free time. Nice to meet you!"


Bonus:
- Add the current date to the end of the paragraph like: "Logged on: 2025-06-14"
-Wrap the printed message with a decorative border of stars (*)
"""

import datetime
name = input("What is your name? ").strip()
age = input("How old are you? ").strip()
city = input("Which city do you live in? ").strip()
profession = input("What is your profession? ").strip()
hobby = input("What is your hobby? ").strip()

intro_message = (
    f"\nHello! My name is {name}. I'm {age} years old and live in {city}."
    f"\nI work as a {profession} and I absolutely enjoy {hobby} in my free time."
    f"\nNice to meet you!\n"
)

current_date = datetime.date.today().isoformat()
intro_message += f"\nLogged on {current_date}\n"

border = "*" * 80
final_output = f"{border}\n{intro_message}\n{border}"

print("\n" + final_output)