import random

previous_answers = []
previous_questions = []
previous_user_answers = []

correct_answers = 0
count = 0
question_amount = 0

def yes_no(prompt):
    while True:
        # creates a variable of the user's input and captalised it
        user_input = input(prompt).upper()
        # Checking the user input
        if user_input == "YES" or user_input == "Y":
            return False
        elif user_input == "NO" or user_input == "N":
            return True
        else:
            print("Please Choose Yes or No (Y/N)")

def float_checker(prompt):
    while True:
        # trys to run the following code
        try:
            # turns input into a float
            return float(input(prompt))
        # if code fails do this and retry
        except:
            print("Please enter a valid Number")

def get_question_types(prompt):
    while True:
        # make the users input captalised
        user_input = input(prompt).upper()
        # Check if user entered a correct answer if so return the input
        if user_input in ["+", "-", "X", "/"]:
            return user_input
        elif user_input in ["ALL"]:
            return ["+", "-", "X", "/"]
        # if user didnt enter correct answer run following code
        else:
            print("Please choose +, X, /, - or all to begin")

def one_question(number):
    global question_types, correct_answers, previous_questions, previous_answers, previous_user_answers
    correct_answer = 0
    print("~~~~~~ Question {} ~~~~~~\n".format(number))
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
    elif question_choice == "X":
        correct_answer = number_one * number_two
    
    # asks for the users anser and makes it a float
    prompt = ("What is {} {} {} rounded to the first decimal place\n".format(number_one, question_choice, number_two))
    user_answer = float_checker(prompt)
    # rounds user and correct answer to the first decimal place
    user_answer = round(user_answer, 1)
    correct_answer = round(correct_answer, 1)

    # checks if the answer is correct
    if correct_answer == user_answer:
        print("Congratulations you got it right!\n")
        correct_answers += 1
    else:
        print("Oh no you got it wrong. The correct answer was {}!".format(correct_answer))
    # adds the history to the lists 
    previous_user_answers.append(user_answer)
    previous_answers.append(correct_answer)
    previous_questions.append(prompt)

#Start menu
print(".___  ___.      ___   .___________. __    __       ______      __    __   __   ________  \n" +
"|   \/   |     /   \  |           ||  |  |  |     /  __  \    |  |  |  | |  | |       /  \n" +
"|  \  /  |    /  ^  \ `---|  |----`|  |__|  |    |  |  |  |   |  |  |  | |  | `---/  /   \n" +
"|  |\/|  |   /  /_\  \    |  |     |   __   |    |  |  |  |   |  |  |  | |  |    /  /    \n" +
"|  |  |  |  /  _____  \   |  |     |  |  |  |    |  `--'  '--.|  `--'  | |  |   /  /----.\n" +
"|__|  |__| /__/     \__\  |__|     |__|  |__|    \_____\______\\________/ |__|  /________|\n" +
"~~~~ BY MAXIAN MOONEY ~~~~\n")


while True:
    # resets the question types when rerun
    question_types = ["+", "/", "-", "x"]
    print("~~~~~~ SETTINGS ~~~~~~")
    # asks what type of operator they want
    question_types = get_question_types("Please choose one of the following operators or type all for all of them (+, X, /, -)\n")
    # asks how many rounds they want to play
    round_input = int(float_checker("How many rounds do you want to play?\n"))
    # for every round they want to play add 1 to the count and run one_question with the count paramater
    for i in range(round_input):
        count += 1
        one_question(count)
    print("~~~~~~ REPLAY ~~~~~~")
    # asks after the code has finished if they want another question
    if (yes_no("Would you like another question? (Y/N)\n")):
        print("~~~~~~ SUMMARY ~~~~~~")
        print("Your Score was {}/{} questions correct!".format(correct_answers, count))
        print("~~~~~~ HISTORY ~~~~~~")
        for i in range(len(previous_questions)):
            print(f"{previous_questions[i]}Correct Answer: {previous_answers[i]}\nYour Answer: {previous_user_answers[i]}")
        print("Thank you for playing come back soon!")
        break