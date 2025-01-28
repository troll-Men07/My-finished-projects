while True:
    print("Please input a number, input Q if you want to quit the program")
    User_Input = input()
    
    if User_Input in ["Q", "q"]:
        print("Quitting the program")
        break
    
    # Convert the input to integer to perform calculations
    try:
        Number = int(User_Input)
    except ValueError:
        print("Please enter a valid number or Q to quit.")
        continue  # Skip the rest of the loop and prompt again if invalid input
    
    while Number != 1:
        if Number % 2 == 0:
            # Even
            Number = Number // 2
            print(Number)
        else:
            # Odd
            Number = Number * 3 + 1
            print(Number)

    print("Finish. Input Q if you want to quit the program.")