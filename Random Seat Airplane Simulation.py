# ================================================================
# ✈️ Airplane Boarding Simulation
# Created entirely with the help of ChatGPT (OpenAI)
# Shared reference: https://chatgpt.com/share/68ff64a5-4968-8001-a397-3d1cf2a49cd1
# ================================================================

import random
import time

print("=== ✈️ Airplane Boarding Simulation ===")

# ---------- Safe Input with Retry or Default ----------
def safe_input(prompt, default, type_func):
    while True:
        user_input = input(prompt)
        if user_input.strip() == "":
            print(f"⚙️ Using default value: {default}")
            return default
        try:
            value = type_func(user_input)
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print(f"❌ Invalid input '{user_input}'")
            choice = input(f"Would you like to use the default ({default}) instead? (y/n): ").lower()
            if choice == "y":
                print(f"✅ Using default value: {default}")
                return default
            else:
                print("↩️ Okay, please try again.\n")

# ---------- User Customizable Inputs ----------
rows = safe_input("Enter number of seat rows (default 5): ", 5, int)
group_size = safe_input("Enter number of passengers per group (default 5): ", 5, int)
total_passengers = safe_input("Enter total passengers (default 10): ", 10, int)
time_to_enter_group = safe_input("Enter time for group to enter (default 2.5): ", 2.5, float)
time_to_sit = safe_input("Enter time for one passenger to sit (default 1): ", 1.0, float)
delay = safe_input("Enter delay between cycles in seconds (default 0.8): ", 0.8, float)

# ---------- System Setup ----------
cols = 3
plane = [[None for _ in range(cols)] for _ in range(rows)]  # layout L, W, R
next_passenger_id = 1
time_elapsed = 0
cycle = 0

def all_seats_full(plane):
    for r in plane:
        if r[0] is None or r[2] is None:
            return False
    return True

# ---------- Simulation Loop ----------
while not all_seats_full(plane):
    cycle += 1
    actions = []

    # Spawn new group
    new_group = []
    for _ in range(group_size):
        if next_passenger_id <= total_passengers:
            new_group.append({'id': next_passenger_id, 'row': len(new_group)})
            next_passenger_id += 1
        else:
            break

    if not new_group:
        break

    # Group enters at once
    for p in new_group:
        if p['row'] < rows:
            plane[p['row']][1] = p['id']
    time_elapsed += time_to_enter_group
    actions.append(f"Group of {len(new_group)} passengers entered (+{time_to_enter_group}s).")

    # Each tries to sit
    for person in new_group:
        row = person['row']
        if row >= rows:
            continue

        left_free = plane[row][0] is None
        right_free = plane[row][2] is None

        if not (left_free or right_free):
            actions.append(f"Passenger {person['id']} found row {row} full, waits.")
            continue

        if left_free and right_free:
            side = random.choice(['left', 'right'])
        elif left_free:
            side = 'left'
        else:
            side = 'right'

        if side == 'left':
            plane[row][0] = person['id']
            actions.append(f"Passenger {person['id']} sat LEFT at row {row}.")
        else:
            plane[row][2] = person['id']
            actions.append(f"Passenger {person['id']} sat RIGHT at row {row}.")
        plane[row][1] = None
        time_elapsed += time_to_sit

    # ---------- Print plane layout ----------
    print(f"\n=== Cycle {cycle} ===")
    for r in range(rows):
        left = plane[r][0] if plane[r][0] else '-'
        walk = plane[r][1] if plane[r][1] else '|'
        right = plane[r][2] if plane[r][2] else '-'
        print(f"Row {r:02}: [{left}] {walk} [{right}]")
    print("Actions:")
    for act in actions:
        print(" •", act)
    print("Total time elapsed:", round(time_elapsed, 2), "seconds")

    time.sleep(delay)

# ---------- End ----------
print("\n✅ All seats are full!")
print("Final layout:")
for r in range(rows):
    print(plane[r])
print("Total time elapsed:", round(time_elapsed, 2), "seco_
