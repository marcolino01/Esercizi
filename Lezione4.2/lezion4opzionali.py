#1. School Grading System:

#Create a function that takes a student's name and their scores in different subjects as input.
#The function calculates the average score and prints the student's name, average, and a 
#message indicating whether the student passed the exam (average >= 60) or failed.
#Create a for loop to iterate over a list of students and scores, calling the function 
#for each student.

import random


def student_grading(student: str, scores : list[int])->str:
    average : int = sum(scores)//len(scores)
    if average >= 60:
        print(f"Congratulation {student},you passed the exam with an average of {average} ")
    else:
        print("Sorry ,you failed the exam")

students : list[str] = ["Marco", "Gaia", "Lorenzo"]
scores_marco : list[int] = [73,68,34]
scores_gaia : list[int] = [81,75,86]
scores_lorenzo : list[int] = [64,52,51]

for i in students:
    if i == "Marco":
        student_grading(i,scores_marco)
    elif i == "Gaia":
        student_grading(i,scores_gaia)
    elif i == "Lorenzo":
        student_grading(i,scores_lorenzo)

#2. Guess the Number Game:
# Create a function that generates a random number within a range specified by the user.
# Prompt the user to guess the number within a specified maximum number of attempts.
# Provide feedback to the user after each guess, indicating whether their guess is too high, too low, or correct.
#Terminate the loop when the user guesses the number correctly or reaches the maximum number of attempts.


range_number : int = int(input("inserisci un numero per il range:->"))
def guess_number(range_number):
    number : int = random.randint(0,range_number)
    user_number : int = int(input("Hai tre tentativi per indovinare il numero.VIAAA"))
    count = 1
    while i<3:
        if user_number != number:
            user_number = int(input("Hai sbagliato ,riprova :->"))
        elif number-10 < user_number < number+10:
            if user_number > number:
                user_number = int(input("Sei vicino riprova con un numero piu basso"))
            else:
                user_number = int(input("Sei vicino riprova con un numero più alto"))
        elif user_number == number:
            print(f"complimenti hai indovinato il numero era : {number}")
            break
        else:
            if user_number > number:
                user_number = int(input("Sei lontano prova con un numero piu piccol0"))
            else:
                user_number = int(input("Sei lontano prova con un numero piu grande"))

    count+=1

