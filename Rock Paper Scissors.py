import random


restart = 1
while restart != "x":
    RPS = ["Rock", "Paper", "Scissors"]
    CPU = random.choice(RPS)

    print("To exit, input x")

    print("Choose between Rock, Paper, Scissors (Must be capitalized to work)")

    print("What would you like to choose?")

    Player = input()

    if Player == "x":
        restart = "x"
        break

    Check_word = (f"{Player}" in RPS)
    if not Check_word:
        print("You typed in the wrong word, please check your answer")
        continue


    print(f"You choose {Player}")

    print(f"CPU: I choose {CPU}")

    if Player == "Rock" and CPU == "Rock":
        print("Draw")
    elif Player == "Rock" and CPU == "Paper":
        print("You lose")
    elif Player == "Rock" and CPU == "Scissors":
        print("You win")
    elif Player == "Paper" and CPU == "Paper":
        print("Draw")
    elif Player == "Paper" and CPU == "Scissors":
        print("You lose")
    elif Player == "Paper" and CPU == "Rock":
        print("You win")
    elif Player == "Scissors" and CPU == "Scissors":
        print("Draw")
    elif Player == "Scissors" and CPU == "Rock":
        print("You lose")
    elif Player == "Scissors" and CPU == "Paper":
        print("You win")

    print("Press enter to restart or x to exit")
    restart = input()
print("Have a nice day, Player")