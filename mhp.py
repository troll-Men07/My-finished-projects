#to generate or manipulate a random integers
import random
#defining the "script()" fucntion
def script():
    #a list containing which door the host can open
    host_door_list = [1, 2, 3]
    #a list containing which door the player can open
    player_door_list = [1,2,3]
    print(f"Host List: {host_door_list}")
    print(f"Player List: {player_door_list}")
    #pick which door will have the prize
    prized_door = random.choice(host_door_list)
    #let the host know which door has the prize and remove that door from the list
    host_door_list.remove(prized_door)
    print(F"Prized Door: {prized_door}")
    print(f"Host List: {host_door_list}")
    print(f"Player List: {player_door_list}")
    #player pick a number 1-3
    player_first_door = random.randint(1,3)
    #remove a number so the player can't choose it again
    player_door_list.remove(player_first_door)
    print(f"Player 1st door: {player_first_door}")
    #check if the player picked number is in the host list
    if player_first_door in host_door_list:
        #if yes then remove the number in the list so the host can't choose it
        host_door_list.remove(player_first_door)

    print(f"Host List: {host_door_list}")
    print(f"Player List: {player_door_list}")
    #the host open the only door available
    host_open_door = random.choice(host_door_list)
    #remove a door based on which door the host opened
    player_door_list.remove(host_open_door)
    #remove a door based on which door the host opened
    host_door_list.remove(host_open_door)
    print(f"Host Open Door: {host_open_door}")
    print(f"Host List: {host_door_list}")
    print(f"Player List: {player_door_list}")
    #just a integers variable incase the player choose again
    player_second_door = int
    #choose a random number 1-2
    choose_again = random.randint(1,2)
    #if the number is 1 then
    if choose_again == 1:
        print("Player Choice: 1 ")
        #the player choose again based on the player door list
        player_second_door = random.choice(player_door_list)
        print(f"Player Open 2nd Door: {player_second_door}")
        #detect if the second choice is equal to the prized door
        if player_second_door == prized_door:
            #if yes then win
            print("Player State: 1")
        else:
            #if no then lose
            print("Player State: 2")
    #if the number is 2 then
    if choose_again == 2:
        print("Player Choice: 2")
        print(f"Player Open 1st Door: {player_first_door}")
        #goes straight into detecting the player first choice 
        if player_first_door == prized_door:
            #just like before, if yes then win
            print("Player State: 1")
        else:
            #if no then lose
            print("Player State: 2")
    #ignore this part, it's not that useful
    #basically assign the "player_state" True or False boolean
    if player_first_door == prized_door:
        player_state = True
    else:
        if player_second_door == prized_door:
            player_state = True
        else:
            player_state = False

    print(player_state)

#add this to run 100 times, delete to run 1 time
for i in range(100):
    script()
