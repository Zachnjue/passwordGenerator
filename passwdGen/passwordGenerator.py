# Implement a simple password generator
import random

# se the character list for generating the password
characters = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ&*()\{\}[]|/\?!@#$%^abcdefghijklmnopqrstuvwxyz"
# Take the length of the password
passwordLength = int(input("Enter the length of the password: "))
# Generate the password
password = "".join(random.sample(characters, passwordLength))
# Print the generated password
print(f"Generated password: {password}")
