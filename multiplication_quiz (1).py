#1/9/25
#Multiplication Quiz

#Init

import random

#Func

def mq():
    grade = 0
    print("Welcome to the multiplication quiz! Each quiz you take will have 5 questions.")
    quiz = input("Would you like to begin?")
    if quiz.lower() == "yes":
        for i in range (5):
            num1 = random.randint(1,12)
            num2 = random.randint(1,12)
            correct_answer = num1*num2
            answer = int(input("What is " + str(num1) + " x " + str(num2)))
            if answer == correct_answer:
                print("Correct!")
                grade = grade + 1
            else:
                print("Incorrect! The correct answer is " + str(correct_answer))
        print("Done! You scored a " + str(grade) + "/5!")

#Main
mq()
