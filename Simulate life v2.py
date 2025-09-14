import random

class Humans:
    def __init__(self):
        self.age = 0
        self.aging_constant = random.randint(1, 3)
        self.alive = True
        self.has_fruit = False
        self.death_chance = 0.30

    def update(self):
        if not self.alive:
            return
        
        self.age += 1
        self.has_fruit = random.random() < 0.4

        # update death chance with aging
        if self.age <= 50:
            self.death_chance = 0.30 + 0.05 * (self.age / 50)
        else:
            self.death_chance = min(1.0, 0.35 + (0.65) * (1 - (50 / self.age) ** self.aging_constant))

        # death check (unless protected by fruit)
        if not self.has_fruit:
            if random.random() < self.death_chance:
                self.alive = False

    def procreate(self, other):
        if self.alive and other.alive and self.has_fruit and other.has_fruit:
            return Humans()
        return None

    def __repr__(self):
        return f"Humans(age={self.age}, alive={self.alive}, fruit={self.has_fruit})"            

def Run_Simulation():
    try:
        Sim_cycle = int(input("How many cycles do you want to do: "))
        Num_humans = int(input("How many humans: "))
    except ValueError:
        print("Please enter valid whole numbers.")
        return
    
    Subjects = [Humans() for _ in range(Num_humans)]

    for cycle in range(Sim_cycle):
        print(f"\nCycle {cycle + 1}")

        for s in Subjects:
            s.update()
            print(" ", s)

        Children = []
        for i in range(len(Subjects)):
            for j in range(i + 1, len(Subjects)):
                Newborn = Subjects[i].procreate(Subjects[j])
                if Newborn is not None:
                    Children.append(Newborn)

        if Children:
            print(f"  {len(Children)} new babies born!")
            Subjects.extend(Children)

        Life_count = sum(1 for s in Subjects if s.alive)
        print(f"Alive humans: {Life_count}")

    print("\nSimulation finished")


# --- Simple rerun loop ---
while True:
    Run_Simulation()
    again = input("Do you want to run another simulation? (y/n): ").strip().lower()
    if again != "y":
        print("Exiting simulation.")
        break
