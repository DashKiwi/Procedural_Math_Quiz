import random

previous_answers = []
previous_questions = []
previous_user_answers = []

correct_answers = 0
count = 0
question_amount = 0

def float_checker(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print("Please enter a valid Number")


def one_question(number):
    global question_types, correct_answers, previous_questions, previous_answers, previous_user_answers
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
    
    #asks for the users anser and makes it a float
    user_answer = float_checker("What is {} {} {} rounded to the first decimal place\n".format(number_one, question_choice, number_two))
    #rounds user and correct answer to the first decimal place
    user_answer = round(user_answer, 1)
    correct_answer = round(correct_answer, 1)

    #checks if the answer is correct
    if correct_answer == user_answer:
        print("Yay you got it right!")
        correct_answers += 1
    else:
        print("Oh no you got it wrong. The correct answer was {}!".format(correct_answer))
    #adds the history to the lists 
    previous_user_answers.append(user_answer)
    previous_answers.append(correct_answer)
    previous_questions.append(number_one)
    previous_questions.append(question_choice)
    previous_questions.append(number_two)

#Start menu
print(".___  ___.      ___   .___________. __    __       ______      __    __   __   ________  \n" +
"|   \/   |     /   \  |           ||  |  |  |     /  __  \    |  |  |  | |  | |       /  \n" +
"|  \  /  |    /  ^  \ `---|  |----`|  |__|  |    |  |  |  |   |  |  |  | |  | `---/  /   \n" +
"|  |\/|  |   /  /_\  \    |  |     |   __   |    |  |  |  |   |  |  |  | |  |    /  /    \n" +
"|  |  |  |  /  _____  \   |  |     |  |  |  |    |  `--'  '--.|  `--'  | |  |   /  /----.\n" +
"|__|  |__| /__/     \__\  |__|     |__|  |__|    \_____\______\\________/ |__|  /________|\n" +
"~~~~ BY MAXIAN MOONEY ~~~~\n")


while True:
    #resets the question types when rerun
    question_types = ["+", "/", "-", "x"]
    #asks what type of operator they want
    user_input = input("Please choose one of the following operators or type any for all of them (+, X, /, -)\n").upper()
    #checks the users answer
    if user_input == "ALL":
        pass
    elif user_input == "+":
        question_types = ["+"]
    elif user_input == "X":
        question_types = ["x"]
    elif user_input == "/":
        question_types = ["/"]
    elif user_input == "-":
        question_types = ["-"]
    else:
        print("Please choose +, X, /, - or all to begin")
    #asks how many rounds they want to play
    user_input = int(input("How many rounds do you want to play?\n"))
    round_number = 0
    #for every round they want to play add 1 to the count and run one_question with the count paramater
    for i in range(user_input):
        count += 1
        one_question(count)
    #asks after the code has finished if they want another question
    user_input = input("Would you like another question? (Y/N)\n").upper()
    #if the user answer is yes it reruns the code in this code block
    if user_input == "YES" or user_input == "Y":         
        pass
    #if the answer is no then end the code
    elif user_input == "NO" or user_input == "N":
        print("~~~~~~ SUMMARY ~~~~~~")
        print("Your Score was {}/{} questions correct!".format(correct_answers, count))
        print("~~~~~~ HISTORY ~~~~~~")
        print("Thank you for playing come back soon!")
        break