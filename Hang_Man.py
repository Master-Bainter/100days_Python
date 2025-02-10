import random

#Allows other player to choose word to use in the game
#Need to be carefull because word is visible to player, need to somehow mask the word
#word = input("Choose a word for the player to guess: ")

#Comment out the two lines below this and create your own random list. Need to update "word" with "word_list"
#throughout the code
word_list = ['boogers', 'chess', 'burger', 'headset', 'cheesecake', 'kickstart', 'desktop', 'mechanical']
word_choice = random.choice(word_list)

word_len = len(word_choice)
placeholder = ""
lives = 6
game_over = False
correct_letters = []
wrong_letters = []

#hangman stages of the game: stages is in reverse, meaning index 6 is the first display to see this
#run a print(stages[6]).
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
    wrong = ""

    for letter in word_choice:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in word_choice:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Lose")

    if "_" not in display:
        game_over = True
        print("You Win")

    print(stages[lives])
