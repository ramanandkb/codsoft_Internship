import random
import string

def generate_password(length=12, use_digits=True, use_special_chars=True):
    characters = string.ascii_letters  # Start with letters

    if use_digits:
        characters += string.digits

    if use_special_chars:
        characters += string.punctuation

    if not characters:
        return "Cannot generate a password with no character set selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    length = int(input("Enter the desired password length: "))
    use_digits = input("Include digits? (yes/no): ").lower().startswith("y")
    use_special_chars = input("Include special characters? (yes/no): ").lower().startswith("y")

    password = generate_password(length, use_digits, use_special_chars)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
