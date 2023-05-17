import random
import string

def generate_password(length=8, include_digits=True, include_symbols=True):
    """Generate a random password with the specified length and optional character sets."""
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password = generate_password(length=10, include_digits=True, include_symbols=True)
print("Generated Password:", password)
