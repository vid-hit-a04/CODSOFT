# Password Generator Program

import random
import string

print("Welcome to Password Generator")

# User input for password length
length = int(input("Enter desired password length: "))

# Define characters to use
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ""

for i in range(length):
    password += random.choice(characters)

# Display password
print("Generated Password:", password)