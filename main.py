import random

question_types = ["+", "/", "-", "x"]

correct_answers = 0
question_count = 0
count = 0
question_amount = 0

def float_checker(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print("Please enter a valid Number")


def one_question(number):
    global question_types, correct_answers, question_count
    correct_answer = 0
    print("Question {}".format(number))
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
    
    user_answer = float_checker("What is {} {} {} rounded to the first decimal place\n".format(number_one, question_choice, number_two))
    user_answer = round(user_answer, 1)
    correct_answer = round(correct_answer, 1)

    if correct_answer == user_answer:
        print("Yay you got it right!")
        correct_answers += 1
    else:
        print("Oh no you got it wrong. The correct answer was {}!".format(correct_answer))

print(".___  ___.      ___   .___________. __    __       ______      __    __   __   ________  \n" +
"|   \/   |     /   \  |           ||  |  |  |     /  __  \    |  |  |  | |  | |       /  \n" +
"|  \  /  |    /  ^  \ `---|  |----`|  |__|  |    |  |  |  |   |  |  |  | |  | `---/  /   \n" +
"|  |\/|  |   /  /_\  \    |  |     |   __   |    |  |  |  |   |  |  |  | |  |    /  /    \n" +
"|  |  |  |  /  _____  \   |  |     |  |  |  |    |  `--'  '--.|  `--'  | |  |   /  /----.\n" +
"|__|  |__| /__/     \__\  |__|     |__|  |__|    \_____\______\\________/ |__|  /________|\n" +
"~~~~ BY MAXIAN MOONEY ~~~~\n")


while True:
    user_input = int(input("How many rounds do you want to play?\n"))
    round_number = 0
    for i in range(user_input):
        count += 1
        one_question(count)
    user_input = input("Would you like another question? (Y/N)\n").upper()
    if user_input == "YES" or user_input == "Y":         
        pass
    elif user_input == "NO" or user_input == "N":
        print("~~~~~~ SUMMARY ~~~~~~")
        print("Your Score was {}/{} questions correct!".format(correct_answers, count))
        print("Thank you for playing come back soon!")
        break