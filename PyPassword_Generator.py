
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []

user_letters = int(input("How many letters would you like? "))
user_numbers = int(input("How many numbers would you like? "))
user_symbols = int(input("How many symbols would you like? "))
#letter_choice = random.choices(letters)

# Add letters
for _ in range(user_letters):
    password.append(random.choice(letters))

# Add numbers
for _ in range(user_numbers):
    password.append(random.choice(numbers))

# Add symbols
for _ in range(user_symbols):
    password.append(random.choice(symbols))

# Shuffle the password list to make it random
random.shuffle(password)

# Convert the list into a string
password = ''.join(password)

print(f"Your generated password is: {password}")

