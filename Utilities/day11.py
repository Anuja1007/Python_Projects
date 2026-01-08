"""
Challenge: Friendship Compatibility Calculator

Build a python script that calculates a fun "compatibility score" between two friends based on their names.

Your program should:
1. Ask for two names (friend A and friend B)
2. Count shared letters, vowels, and character positions to create a compatibility score(0-100).
3. Display the percentage with a themed message like:
    "You're like chai and samosa - made for each other!" or
    "Well... opposites attract, maybe?"

Bonus:
- Use emojis in the result
- Give playful advice based on the score range
- Capitalize and center the final output in a framed box
"""

def friendship_score(name1, name2):
    name1 = name1.lower().strip()
    name2 = name2.lower().strip()

    score = 0
    vowels = set('aeiou')

    # Shared letters
    shared_letters = set(name1) & set(name2)
    shared_letters.discard(" ")

    score += len(shared_letters) * 5
    score += len(vowels & shared_letters) * 10

    # Same character positions
    for a, b in zip(name1, name2):
        if a == b and a != " ":
            score += 7

    return min(score, 100)


def get_message(score):
    if score >= 80:
        return "💖 YOU'RE LIKE CHAI AND SAMOSA — MADE FOR EACH OTHER! 💖\nBESTIES FOR LIFE 🤝"
    elif score >= 60:
        return "😄 GREAT FRIENDSHIP ENERGY!\nKEEP THE VIBES STRONG ✨"
    elif score >= 40:
        return "🙂 WELL... OPPOSITES ATTRACT, MAYBE?\nCOMMUNICATION HELPS 🔑"
    else:
        return "😬 NEEDS SOME WORK!\nPUT IN A LITTLE EXTRA EFFORT 💪"


def print_box(text):
    lines = text.split("\n")
    width = max(len(line) for line in lines) + 4

    print("+" + "-" * width + "+")
    for line in lines:
        print("| " + line.center(width - 2) + " |")
    print("+" + "-" * width + "+")


def run_friendship_calculator():
    print("❤️  FRIENDSHIP COMPATIBILITY CALCULATOR ❤️")
    name1 = input("Enter first name: ")
    name2 = input("Enter second name: ")

    if not name1.strip() or not name2.strip():
        print("\n❌ NAMES CANNOT BE EMPTY!")
        return

    score = friendship_score(name1, name2)
    message = f"COMPATIBILITY SCORE: {score}%\n\n{get_message(score)}"

    print()
    print_box(message.upper())


run_friendship_calculator()
