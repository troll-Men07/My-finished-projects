import random

def script():
    host_door_list = [1, 2, 3]
    player_door_list = [1,2,3]
    print(f"Host List: {host_door_list}")
    print(f"Player List: {player_door_list}")

    prized_door = random.choice(host_door_list)
    host_door_list.remove(prized_door)
    print(F"Prized Door: {prized_door}")
    print(f"Host List: {host_door_list}")
    print(f"Player List: {player_door_list}")

    player_first_door = random.randint(1,3)
    player_door_list.remove(player_first_door)
    print(f"Player 1st door: {player_first_door}")

    if player_first_door in host_door_list:
        host_door_list.remove(player_first_door)

    print(f"Host List: {host_door_list}")
    print(f"Player List: {player_door_list}")

    host_open_door = random.choice(host_door_list)
    player_door_list.remove(host_open_door)
    host_door_list.remove(host_open_door)
    print(f"Host Open Door: {host_open_door}")
    print(f"Host List: {host_door_list}")
    print(f"Player List: {player_door_list}")

    player_second_door = int

    choose_again = random.randint(1,2)

    if choose_again == 1:
        print("Player Choice: 1 ")
        player_second_door = random.choice(player_door_list)
        print(f"Player Open 2nd Door: {player_second_door}")

        if player_second_door == prized_door:
            print("Player State: 1")
        else:
            print("Player State: 2")
    if choose_again == 2:
        print("Player Choice: 2")
        print(f"Player Open 1st Door: {player_first_door}")
        if player_first_door == prized_door:
            print("Player State: 1")
        else:
            print("Player State: 2")

    if player_first_door == prized_door:
        player_state = True
    else:
        if player_second_door == prized_door:
            player_state = True
        else:
            player_state = False

    print(player_state)