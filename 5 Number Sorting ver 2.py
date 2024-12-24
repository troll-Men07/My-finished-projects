import random

First = random.randint(0,100)
Second = random.randint(0,100)
Third = random.randint(0,100)
Fourth = random.randint(0,100)
Fifth = random.randint(0,100)
List_of_numbers = [First, Second, Third, Fourth, Fifth]

print("Before: " + str(First))
print("Before: " + str(Second))
print("Before: " + str(Third))
print("Before: " + str(Fourth))
print("Before: " + str(Fifth))
print("List of numbers before sorted:" + str(List_of_numbers))

First = min(List_of_numbers)
List_of_numbers.remove(First)

Second = min(List_of_numbers)
List_of_numbers.remove(Second)

Third = min(List_of_numbers)
List_of_numbers.remove(Third)

Fourth = min(List_of_numbers)
List_of_numbers.remove(Fourth)

Fifth = min(List_of_numbers)
List_of_numbers.remove(Fifth)

List_of_numbers2 = [First, Second, Third, Fourth, Fifth]

print("After: " + str(First))
print("After: " + str(Second))
print("After: " + str(Third))
print("After: " + str(Fourth))
print("After: " + str(Fifth))
print("List of numbers after sorted:" + str(List_of_numbers2))

LoL = input("Press enter or close to exit the program")