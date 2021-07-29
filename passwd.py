import random
import string
import secrets

print('hello, Welcome to Password generator')

# input the length of password
length = int(input("\n Enter the length of the password: "))

# define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

# combine the data
all = lower + upper + num + symbols

# use secrets
#temp = secrets.choice(all) for i in range(length)

# create the password
password = "".join(secrets.choice(all) for i in range(length))

print(password)
