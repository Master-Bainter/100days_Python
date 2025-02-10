import random

word_list = ['boogers', 'chess', 'burger', 'headset']
word_choice = random.choice(word_list)
word_len = len(word_choice)
placeholder = ""
lives = 6
game_over = False
correct_letters = []

#hangman stages of the game: stages is in reverse, meaning index 6 is the first display to see this
#run a print(stages[6])
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=======
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=======
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=======
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=======
''', r'''
  +---+
  |   |
  O   |
 /    |
      |
      |
=======
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=======
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=======
''']

for position in range(word_len):
    placeholder += "_"
print(placeholder)

while not game_over:
    guess = input("guess a letter: ").lower()
    display = ""

    for letter in word_choice:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if "_" not in display:
        game_over = True
        print("You Win")
