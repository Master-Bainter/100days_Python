#Code below this line
import random

print("""
**************************
*                        *
*    0 - Rock            *
*    1 - Scissors        *
*    2 - Paper           *
*                        *
**************************                
""")
player_1 = int(input("Please select make a selection: "))

# Rock paper scissor vars
rock = ("""
    _______
---'   ____)
      (_____)
rock  (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
paper      _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
scissors_________)
      (____)
---.__(___)
""")
choices = [rock, paper, scissors]
computer_choice = random.choice(choices)

#game code
if player_1 == 0:
    print("You")
    print(choices[0])
    print("Computer")
    print(computer_choice)
    if computer_choice == choices[1]:
        print("Computer Wins!")
    elif computer_choice == choices[0]:
        print("It's a Draw!")
    else:
        print("You Win!")
elif player_1 == 1:
    print("You")
    print(paper)
    print("Computer")
    print(computer_choice)
    if computer_choice == choices[2]:
        print("Computer Wins!")
    elif computer_choice == choices[1]:
        print("It's a Draw!")
    else:
        print("You Win!")
else:
    print("You")
    print(scissors)
    print("Computer")
    print(computer_choice)
    if computer_choice == choices[0]:
        print("Computer Wins!")
    elif computer_choice == choices[2]:
        print("It's a Draw!")
    else:
        print("You Win!")
