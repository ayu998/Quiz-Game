# Quiz game
import random

questions = ["What is the capital of India?",
             "Which planet is known as the Red Planet?",
             "Who is known as the Father of the Nation in India?",
             "Which is the largest ocean on Earth?",
             "How many continents are there on Earth?",
             "Which gas do plants absorb from the atmosphere?",
             "What is the national animal of India?",
             "Who invented the telephone?",
             "Which is the smallest prime number?",
             "Which river is called the Ganga of South India?"]

answers = ["New Delhi", "Mars", "Mahatma Gandhi", "Pacific Ocean", "7",
           "Carbon Dioxide", "Bengal Tiger", "Alexander Graham Bell",
           "2", "Godavari"]

options = [["A) Mumbai","B) New Delhi","C) Kolkata","D) Chennai"],
           ["A) Venus","B) Jupiter","C) Mars","D) Saturn"],
           ["A) Jawaharlal Nehru", "B) Sardar Patel", "C) Bhagat Singh", "D) Mahatma Gandhi"],
           ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
           ["A) 5", "B) 6", "C) 7", "D) 8"],
           ["A) Oxygen", "B) Carbon Dioxide", "C) Nitrogen", "D) Hydrogen"],
           ["A) Lion", "B) Elephant", "C) Tiger", "D) Peacock"],
           ["A) Thomas Edison", "B) Alexander Graham Bell", "C) Nikola Tesla", "D) Isaac Newton"],
           ["A) 0", "B) 1", "C) 2", "D) 3"],
           ["A) Godavari", "B) Krishna", "C) Kaveri", "D) Narmada"]]
score = 0
while True:
    question = random.choice(questions)

    if question == questions[0]:
        print(questions[0])
        for option in options[0]:
            print(option)
        answer = input("Enter your answer (A/B/C/D): ")
        if answer.upper() == "B":
            score += 1
        else:
            print(f"Wrong answer! The correct answer is {answers[0]}")
    elif question == questions[1]:
        print(questions[1])
        for option in options[1]:
            print(option)
        answer = input("Enter your answer (A/B/C/D): ")
        if answer.upper() == "C":
            score += 1
        else:
            print(f"Wrong answer! The correct answer is {answers[1]}")
    elif question == questions[2]:
        print(questions[2])
        for option in options[2]:
            print(option)
        answer = input("Enter your answer (A/B/C/D): ")
        if answer.upper() == "D":
            score += 1
        else:
            print(f"Wrong answer! The correct answer is {answers[2]}")
    elif question == questions[3]:
        print(questions[3])
        for option in options[3]:
            print(option)
        answer = input("Enter your answer (A/B/C/D): ")
        if answer.upper() == "D":
            score += 1
        else:
            print(f"Wrong answer! The correct answer is {answers[3]}")
    elif question == questions[4]:
        print(questions[4])
        for option in options[4]:
            print(option)
        answer = input("Enter your answer (A/B/C/D): ")
        if answer.upper() == "C":
            score += 1
        else:
            print(f"Wrong answer! The correct answer is {answers[4]}")
    elif question == questions[5]:
        print(questions[5])
        for option in options[5]:
            print(option)
        answer = input("Enter your answer (A/B/C/D): ")
        if answer.upper() == "B":
            score += 1
        else:
            print(f"Wrong answer! The correct answer is {answers[5]}")
    elif question == questions[6]:
        print(questions[6])
        for option in options[6]:
            print(option)
        answer = input("Enter your answer (A/B/C/D): ")
        if answer.upper() == "C":
            score += 1
        else:
            print(f"Wrong answer! The correct answer is {answers[6]}")
    elif question == questions[7]:
        print(questions[7])
        for option in options[7]:
            print(option)
        answer = input("Enter your answer (A/B/C/D): ")
        if answer.upper() == "B":
            score += 1
        else:
            print(f"Wrong answer! The correct answer is {answers[7]}")
    elif question == questions[8]:
        print(questions[8])
        for option in options[8]:
            print(option)
        answer = input("Enter your answer (A/B/C/D): ")
        if answer.upper() == "B":
            score += 1
        else:
            print(f"Wrong answer! The correct answer is {answers[8]}")
    elif question == questions[9]:
        print(questions[9])
        for option in options[9]:
            print(option)
        answer = input("Enter your answer (A/B/C/D): ")
        if answer.upper() == "A":
            score += 1
        else:
            print(f"Wrong answer! The correct answer is {answers[9]}")
    print(f"Your score is: {score}/10")
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break
