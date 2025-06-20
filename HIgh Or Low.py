import random

def TheGame():
    Deck = [1,2,3,4,5,6,7,8,9,10,11,12]
    RNG = random.randint(0,len(Deck) - 1)
    First_Card = Deck.pop(RNG)
    while len(Deck) != 0:
        RNG = random.randint(0,len(Deck) - 1)
        Second_Card = Deck.pop(RNG)

        print("First Card is: " + str(First_Card))
        print("What is the second card? Higher or Lower than " + str(First_Card) + "?")

        Player = str(input("Higher or Lower: ")).lower()

        if Player not in ["higher", "h", "lower", "l"]:
            print("Invalid input. Please enter 'higher' or 'lower'.")
            continue

        if Player == "higher" or Player == "h":
            if Second_Card > First_Card:
                print("You guessed right! The second card is: " + str(Second_Card))
                print("\033[92mYou win this round!\033[0m")
                print("Let's continue to the next round.")
                print("----------------------------------------")
                print("Cards left in the deck: " + str(len(Deck)))
            else:
                print("You guessed wrong! The second card is: " + str(Second_Card))
                print("\033[91mYou lose and restart from the start.\033[0m")
                print("\033[91mRestarting the game...\033[0m")
                print("----------------------------------------")
                return TheGame()
        else:
            if Second_Card < First_Card:
                print("You guessed right! The second card is: " + str(Second_Card))
                print("\033[92mYou win this round!\033[0m")
                print("Let's continue to the next round.")
                print("----------------------------------------")
                print("Cards left in the deck: " + str(len(Deck)))
            else:
                print("You guessed wrong! The second card is: " + str(Second_Card))
                print("\033[91mYou lose and restart from the start.\033[0m")
                print("\033[91mRestarting the game...\033[0m")
                print("----------------------------------------")
                return TheGame()   
                 
        First_Card = Second_Card
    print("\033[92mCongratulations! You win the game! There are no cards left in the deck.\033[0ml")

def Introduction():
    print("Welcome to the High or Low game!")
    print("You will be given a card, and you must guess if the next card is higher or lower.")
    print("If you guess correctly, you win the round. If not, you lose and restart from the start.")
    print("Let's start the game!")
    TheGame()

Introduction()