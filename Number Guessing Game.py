import random

minNum = 0
maxNum = 0

def AskDifficulty():
    global minNum
    global maxNum
    while True:
        try:
            IsDifficulty = int(input("Please pick your difficulty (1-5): "))
            if IsDifficulty in [1,2,3,4,5]:
                break
            else:
                print("Please put the number 1-5")
        except ValueError:
            print("Please select from the number 1-5")

    #Easy
    if IsDifficulty == 1:
        print("You've picked Easy")
        minNum = 0
        maxNum = 25

    #Normal
    elif IsDifficulty == 2:
        print("You've picked Normal")
        minNum = 0
        maxNum = 50

    #Medium
    elif IsDifficulty == 3:
        print("You've picked Medium")
        minNum = 0
        maxNum = 75

    #Hard
    elif IsDifficulty == 4:
        print("You've picked Hard")
        minNum = 0
        maxNum = 100
        
    #Custom numbers
    elif IsDifficulty == 5:
        print("You've picked Custom Range")
        while True:
            try:
                minNum = int(input("Please input the minimum number: "))
                maxNum = int(input("Please input the maximum number: "))
            except ValueError:
                print("Please place the numbers you want to guess")

            if maxNum > minNum:
                break
            else:
                print("Please put the minimum number lower than the maximum, duh")

def LowerHigher():
    global minNum
    global maxNum
    The_Number = random.randint(minNum, maxNum)
    while True:
        try:
            Player = int(input("Guess the number: "))
        except ValueError:
            print("Please place a number you want to guess")

        if Player == The_Number:
            print("Congratulation You win, yep that's it. Bye")
            break
        elif Player > The_Number:
            print("Lower!")
        elif Player < The_Number:
            print("Higher!")

def TheGame():
    print("Welcome to the Higher Or Lower game")
    print("There are 4 difficulty and custom range")
    print("1. Easy (0-25)")
    print("2. Normal (0-50)")
    print("3. Medium (0-75)")
    print("4. Hard (0-100)")
    print("5. Custom range")
    print("------------------------------------------------")

    AskDifficulty()
    LowerHigher()
    

TheGame()
    