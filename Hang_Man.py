import random

word_list = ['boogers', 'chess', 'burger', 'headset']
word_choice = random.choice(word_list)
word_len = len(word_choice)
placeholder = ""
display = ""
num = 0

print(word_choice)
guess = input("guess a letter: ").lower()

for position in range(word_len):
    placeholder += "_"
print(placeholder)

for letter in word_choice:
    if letter == guess:
        display += letter
    else:
        display += "_"
print(display)
