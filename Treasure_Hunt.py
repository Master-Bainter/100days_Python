#Code below this line

print(r'''
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\/
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \/"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\/
 \_/__________________________________________________________________/
''')

print("Welcome to Treasure Island!")

direction = input("You come to an intersection, do you want to go Left or Right? ").lower()
travel = ""
door = ""

while direction not in ["left", "right"]:
    direction = input("You have to go left or right: ")
if direction == "left":
    travel = input(
        "You come to a lake, with an Island in the middle, do you want to swim or wait for a boat (swim or wait) ").lower()
    while travel not in ["swim", "wait"]:
        travel = input("You have to swim or wait for a boat! ")
    if travel == "wait":
        door = input("You come to 3 doors, Red, Yellow, and Blue. Which one do you want to open? ").lower()
        while door not in ["red", "yellow", "blue"]:
            door = input("You made a wrong selection, try again! ").lower()
        if door == "yellow":
            print("You Win!")
        else:
            print("Game Over")
    else:
        print("Game Over!")
else:
    print("Game Over!")


        #if door == "yellow":
         #   print("You Win!")
        #else:
         #   print("Game Over!")
