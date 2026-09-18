# Password Generator

import random
import string

print(" Password Generator")

# Ask the user for password length
length = int(input("Enter password length: "))

# Characters to use
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ""

for i in range(length):
    password += random.choice(characters)

print("\nGenerated Password:")
print(password)

print("\nPassword generated successfully!")