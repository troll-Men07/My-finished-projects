import random

Chamber = ["L", "W", "W", "W", "W", "W"]
Selecting_mode = ["1","2"]

Shoot_to_word = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "ninth",
    10: "tenth"
}

def spun_once():
    random.shuffle(Chamber)
    print(Chamber)
    Shots = Chamber.pop()
    Shoot = 1

    while Shots != "L":
        print(Chamber)
        Shots = Chamber.pop()
        Shoot += 1
    else:
        word = Shoot_to_word.get(Shoot, f"{Shoot}th")
        print("You lost on the " + str(word) + " shot")
        print("")

def spun_until_lost():
    random.shuffle(Chamber)
    print(Chamber)
    Shots = Chamber.pop()
    Shoot = 1
    while Shots != "L":
        print(Chamber)
        random.shuffle(Chamber)
        Shots = Chamber.pop()
        Shoot += 1
    else:
        word = Shoot_to_word.get(Shoot, f"{Shoot}th")
        print("You lost on the " + str(word) + " shot")
        print("")

restart = 0

while restart != 1:
    Chamber = ["L", "W", "W", "W", "W", "W"]
    print("Which way do you want to play?")
    print("Do you want the chamber to be spun once or after every shots?")
    print("Type 1 if you want it to be spun once or type 2 if you want it to be spun after every shots")
    print("Press enter if you have chosen the way you want to play")
    print("Pressing enter without putting anything will quit the program")

    Player = input()
    if Player == "1":
        spun_once()
    elif Player == "2":
        spun_until_lost()
    elif Player == "":
        restart = 1    
    else:
        print("")
        print("You didn't type the correct mode, please type it correctly")
        print("")
