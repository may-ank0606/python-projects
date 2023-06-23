import random
import string


def generate_password(length=8, uppercase=True, lowercase=True, digits=True, special_chars=True):
    """
    Generate a random password based on the specified criteria.

    Args:
        length (int): Length of the password (default is 8).
        uppercase (bool): Include uppercase letters (default is True).
        lowercase (bool): Include lowercase letters (default is True).
        digits (bool): Include digits (default is True).
        special_chars (bool): Include special characters (default is True).

    Returns:
        str: Generated password.
    """
    characters = ""

    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type should be selected.")

    password = random.choices(characters, k=length)
    return ''.join(password)


# Example usage
length = int(input("Enter the length of the password: "))
uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
digits = input("Include digits? (y/n): ").lower() == 'y'
special_chars = input("Include special characters? (y/n): ").lower() == 'y'

password = generate_password(length, uppercase, lowercase, digits, special_chars)
print("Generated Password:", password)
