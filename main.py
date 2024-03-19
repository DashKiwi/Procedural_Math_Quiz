import random

question_types = ["+", "/", "-", "x"]

correct_answers = 0
question_count = 0


def one_question():
    global question_types, correct_answers, question_count
    correct_answer = 0
    print("Question ")
    # Chooses 2 random numbers
    number_one = random.randrange(1, 20)
    number_two = random.randrange(1, 20)
    question_choice = random.choice(question_types)

    # Detect question type and do the calculations
    if question_choice == "+":
        correct_answer = number_one + number_two
    elif question_choice == "/":
        correct_answer = number_one / number_two
    elif question_choice == "-":
        correct_answer = number_one - number_two
    elif question_choice == "x":
        correct_answer = number_one * number_two

    user_answer = float_checker(input("What is {} {} {}\n".format(number_one, question_choice, number_two)))
    question_count += 1

    if correct_answer == user_answer:
        print("Yay you got it right!")
        correct_answers += 1
    else:
        print("Oh no you got it wrong. The correct answer was {}!".format(correct_answer))


question_amount = input("How many Questions do you want?\n")

for i in question_amount:
    one_question()

print("Thank you for playing your total score was {}/{}".format(0, question_count))
