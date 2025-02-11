# Code below this line
from operator import truediv


# def life_in_weeks(int):
#     x = 52 * 90 - (52 * int)
#     print(f"You have {x} weeks left!")
#
#
# life_in_weeks(int(input("How old are you? ")))

# def greet_with_name(a = "", b = ""):
#     print(f"Hi my name is {a} and I am from {b}")
#
# greet_with_name(b="Brooklyn", a="Harris")



def calculate_love_score(fname, sname):
    true = "true"
    love = "love"
    true_match = []
    love_match = []
    true_count = {}
    love_count = {}
    names = []

    for letters in fname:
        names.append(letters)
    #print(names)

    for letters in sname:
        names.append(letters)
    #print(names) debugging purposes

    for char in names:
        if char in true:
            true_match.append(char)

    for char in names:
        if char in love:
            love_match.append(char)

    for letters in true:
        true_count[letters] = 0

    for letters in love:
        love_count[letters] = 0

    for match in true_match:
        if match in true_count:
            true_count[match] += 1

    for match in love_match:
        if match in love_count:
            love_count[match] += 1

    for letter in true_count:
        print(f"'{letter}' appears {true_count[letter]} times.")
    print("\n\n")
    for letter in love_count:
        print(f"'{letter}' appears {love_count[letter]} times.")




calculate_love_score(input("What is your name? "), input("What is your name? "))
#calculate_love_score("shawn", "heather")