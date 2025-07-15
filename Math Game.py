import random

def GetDifficulty():
    print("Please choose the difficulty you want to play")
    print("1. Easy")
    print("2. Normal")
    print("3. Medium")
    print("4. Hard")

    while True:
        try:
            Difficulty = int(input("(1/2/3/4): "))
            if Difficulty in [1, 2, 3, 4]:
                return Difficulty
            else:
                print("Please choose a valid number between 1 and 4.")
        except ValueError:
            print("Please enter a number.")

def GetQuestion(Difficulty):
    if Difficulty == 1:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        op = random.choice(["+", "-"])
    elif Difficulty == 2:
        a = random.randint(20, 40)
        b = random.randint(20, 40)
        op = random.choice(["+", "-"])
    elif Difficulty == 3:
        a = random.randint(10, 20)
        b = random.randint(10, 20)
        op = random.choice(["*", "/"])
    elif Difficulty == 4:
        a = random.randint(2, 5)
        b = random.randint(2, 4)
        op = random.choice(["^", "*", "/"])

    if op == "+":
        answer = a + b
    elif op == "-":
        answer = a - b
    elif op == "*":
        answer = a * b
    elif op == "/":
        answer = round(a / b, 2)
    elif op == "^":
        answer = a ** b

    question = f"{a} {op} {b} = ?"
    return question, answer

def GenerateOptions(correct_answer):
    options = [correct_answer]
    while len(options) < 5:
        wrong = correct_answer + random.randint(-10, 10)
        if wrong != correct_answer and wrong not in options:
            options.append(wrong)
    random.shuffle(options)
    return options

def Math_Quiz():
    print("Welcome to my Math Quiz")

    while True:
        try:
            num_questions = int(input("How many questions do you want? "))
            break
        except ValueError:
            print("Please enter a number.")

    difficulty = GetDifficulty()
    score = 0

    for i in range(num_questions):
        print(f"\nQuestion {i + 1}:")
        question, correct_answer = GetQuestion(difficulty)
        options = GenerateOptions(correct_answer)

        print(question)
        for idx, opt in enumerate(options):
            print(f"{chr(97 + idx)}. {opt}")  # a. b. c. d. e.

        while True:
            user_input = input("Your answer (a/b/c/d/e): ").lower()
            if user_input in ['a', 'b', 'c', 'd', 'e']:
                selected = options[ord(user_input) - 97]
                if selected == correct_answer:
                    print("✅ Correct!")
                    score += 1
                else:
                    print(f"❌ Wrong! The correct answer was {correct_answer}")
                break  # exit the input loop once answered
            else:
                print("Invalid choice. Please enter a, b, c, d, or e.")


    print(f"\nQuiz finished! Your score: {score}/{num_questions}")

Math_Quiz()