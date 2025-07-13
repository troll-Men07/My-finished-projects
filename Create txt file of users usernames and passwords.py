import os

#Get user's desktop path
GetDesktopPath = os.path.join(os.path.expanduser("~"),"Desktop")

#File path for the User Data txt file
FilePath = os.path.join(GetDesktopPath,"User Data.txt")

def RegisterAnAccount():
    #Get user's username
    GetUsername = input("What is your username? ")
    UserConfirmation = input(f"Is your username {GetUsername}? ")      
    while UserConfirmation.lower() not in ["y", "yes"]:
        if UserConfirmation.lower() in ["y", "yes"]:
            break
        else:
            GetUsername = input("What is your username? ")
            UserConfirmation = input(f"Is your username {GetUsername}? ")
            continue
    #Get user's password
    GetPassword = input("What is your password? ")
    UserConfirmation = input(f"Is your password {GetPassword}? ")      
    while UserConfirmation.lower() not in ["y", "yes"]:
        if UserConfirmation.lower() in ["y", "yes"]:
            break
        else:
            GetPassword = input("What is your password? ")
            UserConfirmation = input(f"Is your password {GetPassword}? ")
            continue
    #Combine user's username and password
    CombineUserData = f"{GetUsername},{GetPassword}"
    #Write user's username and password into a txt file
    with open(FilePath, "a") as file:
        file.write(CombineUserData + "\n")

    print("You have successfully registered an account")

def LoginToAccount():    
    ListOfUserData = []
    IsLogin = input("Do you want to login into your account? (y/n) ")

    if IsLogin in ["y", "yes"]:
        #Get user's username
        GetUsername = input("What is your username? ")
        UserConfirmation = input(f"Is your username {GetUsername}? ")      
        while UserConfirmation.lower() not in ["y", "yes"]:
            if UserConfirmation.lower() in ["y", "yes"]:
                break
            else:
                GetUsername = input("What is your username? ")
                UserConfirmation = input(f"Is your username {GetUsername}? ")
                continue
        #Get user's password
        GetPassword = input("What is your password? ")
        UserConfirmation = input(f"Is your password {GetPassword}? ")      
        while UserConfirmation.lower() not in ["y", "yes"]:
            if UserConfirmation.lower() in ["y", "yes"]:
                break
            else:
                GetPassword = input("What is your password? ")
                UserConfirmation = input(f"Is your password {GetPassword}? ")
                continue
        
        #Combine user's username and password
        CombineUserData = f"{GetUsername},{GetPassword}"

        #Check user's username and password
        try:
            with open(FilePath, "r") as file:
                ListOfUserData = [line.strip() for line in file.readlines()]

        except FileNotFoundError:
            with open(FilePath, "w") as file:
                file.write("")

        if CombineUserData in ListOfUserData:
            print("You have succesfully logged into an account!")
        else:
            print("You haven't registered an account")
    
#Ask user if they want to register or login
IsRegister = input("Do you want to register an account? (y/n) ")

while True:
    if IsRegister.lower() in ["y", "yes"]:
        RegisterAnAccount()
    else:
        LoginToAccount()
        User = input("Do you want to exit the program? (y/n)")
        if User in ["y", "yes"]:
            break
        else:
            IsRegister = input("Do you want to register an account? (y/n) ")