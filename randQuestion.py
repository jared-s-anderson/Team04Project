from GAME_VARIABLES import *
from os import chdir
import random

def question(level):

    # Determine the kind of problem
    # based on your level.
    # If your level is less than 5 you only get addition and subtraction. 
    # When your level is greater than 10 you get 2 digit numbers up to 99.
    sign = 0
    A = 0
    B = 0

    if level <= 5:
        sign = random.randint(0, 1)
    elif level > 5:
        sign = random.randint(0, 3)


    if level == 1:
        A = random.randint(0, 9)
        B = random.randint(0, 9)
    elif level > 1 and level < 10:
        A = random.randint(0, 20)
        B = random.randint(0, 9)
    else:
        A = random.randint(0, 99)
        B = random.randint(0, 99)
    

    if sign == 0:
        answer = A + B
        return 'What is the sum of ' + str(A) + ' + ' + str(B) + '?', answer
    elif sign == 1:
        answer = A - B
        return 'What is the diffrence of ' + str(A) + ' - ' + str(B) + '?', answer
    elif sign == 2:
        answer = A * B
        return 'What is the product of ' + str(A) + ' x ' + str(B) + '?', answer
    else:
        answer = round(A / B, 1)
        dividedBy = str(' ' + chr(247) + ' ')
        return 'What is the quotient of ' + str(A) + dividedBy + str(B) + ' to the nearest 10th?', answer

def checkSolution(user_text, solution):

    try:
        # check the answer, plus the cheat code is 42
        if float(user_text) == solution or float(user_text) == cheatAns:
            return 'Correct!'
        else:
            return 'Incorect:'
    except:
        # In the event converting user_text to a float fails
        # (for example if its not numbers) parse out the problematic
        # characters.
        junk = ''
        for character in user_text:
            if not character.isdigit():
                junk += ("'" + character + "' ")

        return 'Error: Numbers only please!\n' + junk + 'are/is not valid!'