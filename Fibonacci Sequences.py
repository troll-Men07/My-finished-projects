def main():
    print("How many Fibonacci sequences do you want to generate?")
    Number_Of_Sequences = int(input("Entter the number of sequences: "))
    x = 0
    a = 0
    b = 1
    c = a + b
    print(f"Fibonacci Sequence a: {a}")
    print(f"Fibonacci Sequence b: {b}")
    while x != Number_Of_Sequences:
        print(f"Fibonacci Sequence c: {c}")
        a = b
        b = c
        c = a + b
        x += 1
    print("Fibonacci sequence generatioin completed.")
main()