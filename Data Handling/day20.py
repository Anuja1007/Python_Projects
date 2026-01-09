"""
Challenge: Offline Credential Manager

Create a CLI tool to manage login credentials (website, username, password) in an encoded local file (`vault.txt`).

Your program should:
1. Add new credentials (website, username, password)
2. Automatically rate password strength (weak/medium/strong)
3. Encode the saved content using Base64 for simple offline obfuscation
4. View all saved credentials (decoding them)
5. Update password for any existing website entry (assignment)

Bonus:
- Support searching for a website entry
- Mask password when showing in the list
"""

import base64
import os

VAULT_FILE = "vault.txt"


def encode(text):
    return base64.b64encode(text.encode("utf-8")).decode("utf-8")


def decode(text):
    return base64.b64decode(text.encode("utf-8")).decode("utf-8")


def password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*().,<>" for c in password)

    score = sum([length >= 8, has_upper, has_digit, has_special])
    return ["Weak", "Medium", "Strong", "Very Strong"][min(score, 3)]


def add_credential():
    website = input("Website: ").strip()
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if not website or not username or not password:
        print("All fields are required.")
        return

    strength = password_strength(password)
    print(f"Password strength: {strength}")

    line = f"{website}||{username}||{password}"
    encoded_line = encode(line)

    with open(VAULT_FILE, "a", encoding="utf-8") as f:
        f.write(encoded_line + "\n")

    print("✅ Credential saved")


def view_credentials():
    if not os.path.exists(VAULT_FILE):
        print("No credentials found.")
        return

    print("\nSaved credentials:")
    with open(VAULT_FILE, "r", encoding="utf-8") as f:
        for line in f:
            decoded = decode(line.strip())
            website, username, password = decoded.split("||")
            hidden_password = "*" * len(password)
            print(f"{website} | {username} | {hidden_password}")


def update_password():
    if not os.path.exists(VAULT_FILE):
        print("No credentials to update.")
        return

    website_to_update = input("Enter website to update password: ").strip()
    new_password = input("Enter new password: ").strip()

    strength = password_strength(new_password)
    print(f"Password strength: {strength}")

    updated = False
    updated_lines = []

    with open(VAULT_FILE, "r", encoding="utf-8") as f:
        for line in f:
            decoded = decode(line.strip())
            website, username, password = decoded.split("||")

            if website.lower() == website_to_update.lower():
                decoded = f"{website}||{username}||{new_password}"
                updated = True

            updated_lines.append(encode(decoded))

    if not updated:
        print("Website not found.")
        return

    with open(VAULT_FILE, "w", encoding="utf-8") as f:
        for line in updated_lines:
            f.write(line + "\n")

    print("✅ Password updated successfully")


def main():
    while True:
        print("\n🔒 Credential Manager")
        print("1. Add credential")
        print("2. View credentials")
        print("3. Update password")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        match choice:
            case "1":
                add_credential()
            case "2":
                view_credentials()
            case "3":
                update_password()
            case "4":
                print("Goodbye 👋")
                break
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()
