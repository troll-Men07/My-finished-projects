import random

def Custom_Input():
    print("\n--- Gambler's Simulation (Custom Mode) ---")
    Gambler = int(input("Enter initial score: "))
    Target_Goal = int(input("Enter the goal for the gambler to reach: "))
    The_Chance_Of_Winning = int(input("Enter the gambler's winning chance (1-100): "))
    
    Initial_Score = Gambler
    Highest_Score = Gambler
    Lowest_Score = Gambler
    Number_Of_Bets_Made = 0
    Wins = 0
    Loses = 0

    Chances = The_Chance_Of_Winning / 100  

    print(f"\nStarting simulation...")
    print(f"Initial Score: {Initial_Score}, Target Goal: {Target_Goal}, Winning Chance: {The_Chance_Of_Winning}%\n")

    while True:      
        if random.random() < Chances:
            Gambler += 20
            Highest_Score = max(Highest_Score, Gambler)
            Wins += 1
        else:
            Gambler -= 20
            Lowest_Score = min(Lowest_Score, Gambler)
            Loses += 1

        Number_Of_Bets_Made += 1

        print(f"Current Score: {Gambler} | Highest: {Highest_Score} | Lowest: {Lowest_Score} | Bets: {Number_Of_Bets_Made}")

        if Gambler >= Target_Goal:
            print(f"\n🎉 The gambler has reached the goal of {Gambler}! 🎉")
            break
        if Gambler < 0:
            print(f"\n💸 The gambler has lost all their money and is now in debt: {Gambler} 💸")
            break

    print("\n--- Simulation Results ---")
    print(f"Initial Score: {Initial_Score}")
    print(f"Target Goal: {Target_Goal}")
    print(f"Winning Chance: {The_Chance_Of_Winning}%")
    print(f"Total Bets Made: {Number_Of_Bets_Made}")
    print(f"Total Wins: {Wins}")
    print(f"Total Losses: {Loses}")
    print(f"Highest Score Reached: {Highest_Score}")
    print(f"Lowest Score Reached: {Lowest_Score}\n")


def Random_Input():
    print("\n--- Gambler's Simulation (Random Mode) ---")
    Gambler = random.randint(1, 1000)
    Target_Goal = random.randint(2, 10000)
    The_Chance_Of_Winning = random.randint(1, 100)
    
    Initial_Score = Gambler
    Highest_Score = Gambler
    Lowest_Score = Gambler
    Number_Of_Bets_Made = 0
    Wins = 0
    Loses = 0

    Chances = The_Chance_Of_Winning / 100  

    print(f"\nStarting simulation...")
    print(f"Initial Score: {Initial_Score}, Target Goal: {Target_Goal}, Winning Chance: {The_Chance_Of_Winning}%\n")

    while True:      
        if random.random() < Chances:
            Gambler += 20
            Highest_Score = max(Highest_Score, Gambler)
            Wins += 1
        else:
            Gambler -= 20
            Lowest_Score = min(Lowest_Score, Gambler)
            Loses += 1

        Number_Of_Bets_Made += 1

        print(f"Current Score: {Gambler} | Highest: {Highest_Score} | Lowest: {Lowest_Score} | Bets: {Number_Of_Bets_Made}")

        if Gambler >= Target_Goal:
            print(f"\n🎉 The gambler has reached the goal of {Gambler}! 🎉")
            break
        if Gambler < 0:
            print(f"\n💸 The gambler has lost all their money and is now in debt: {Gambler} 💸")
            break

    print("\n--- Simulation Results ---")
    print(f"Initial Score: {Initial_Score}")
    print(f"Target Goal: {Target_Goal}")
    print(f"Winning Chance: {The_Chance_Of_Winning}%")
    print(f"Total Bets Made: {Number_Of_Bets_Made}")
    print(f"Total Wins: {Wins}")
    print(f"Total Losses: {Loses}")
    print(f"Highest Score Reached: {Highest_Score}")
    print(f"Lowest Score Reached: {Lowest_Score}\n")


def Preset_Input():
    print("\n--- Gambler's Simulation (Preset Mode) ---")
    
    Gambler = int(input("Enter initial score: "))
    Target_Goal = int(input("Enter the goal for the gambler to reach: "))

    print("\nChoose a preset chance of winning:")
    print("1. Impossible (10%)")
    print("2. Barely (30%)")
    print("3. Fair (50%)")
    print("4. Likely (70%)")
    print("5. Certain (90%)")

    choice = input("Enter the number of your choice: ")
    
    chances_dict = {
        "1": 10,
        "2": 30,
        "3": 50,
        "4": 70,
        "5": 90
    }

    if choice not in chances_dict:
        print("Invalid choice! Defaulting to Fair (50%).")
        The_Chance_Of_Winning = 50
    else:
        The_Chance_Of_Winning = chances_dict[choice]

    Initial_Score = Gambler
    Highest_Score = Gambler
    Lowest_Score = Gambler
    Number_Of_Bets_Made = 0
    Wins = 0
    Loses = 0

    Chances = The_Chance_Of_Winning / 100  

    print(f"\nStarting simulation...")
    print(f"Initial Score: {Initial_Score}, Target Goal: {Target_Goal}, Winning Chance: {The_Chance_Of_Winning}%\n")

    while True:      
        if random.random() < Chances:
            Gambler += 20
            Highest_Score = max(Highest_Score, Gambler)
            Wins += 1
        else:
            Gambler -= 20
            Lowest_Score = min(Lowest_Score, Gambler)
            Loses += 1

        Number_Of_Bets_Made += 1

        print(f"Current Score: {Gambler} | Highest: {Highest_Score} | Lowest: {Lowest_Score} | Bets: {Number_Of_Bets_Made}")

        if Gambler >= Target_Goal:
            print(f"\n🎉 The gambler has reached the goal of {Gambler}! 🎉")
            break
        if Gambler < 0:
            print(f"\n💸 The gambler has lost all their money and is now in debt: {Gambler} 💸")
            break

    print("\n--- Simulation Results ---")
    print(f"Initial Score: {Initial_Score}")
    print(f"Target Goal: {Target_Goal}")
    print(f"Winning Chance: {The_Chance_Of_Winning}%")
    print(f"Total Bets Made: {Number_Of_Bets_Made}")
    print(f"Total Wins: {Wins}")
    print(f"Total Losses: {Loses}")
    print(f"Highest Score Reached: {Highest_Score}")
    print(f"Lowest Score Reached: {Lowest_Score}\n")


print("🎲 Welcome to the Gambler's Simulation! 🎲")
print("Choose a mode to start:")
print("1. Random Mode - Watch a simulation with randomly generated values.")
print("2. Custom Mode - Enter your own values for a personalized simulation.")
print("3. Preset Mode - Select from preset winning chances.")

Player = input("Which mode do you want to play? (1, 2, or 3): ")
if Player == "1":
    Random_Input()
elif Player == "2":
    Custom_Input()
else:
    Preset_Input()