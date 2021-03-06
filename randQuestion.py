import random

def question(level):

    # Determine the kind of problem based on your level.
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
        return 'What is the sum of {} + {}?'.format(A, B), answer
    elif sign == 1:
        answer = A - B
        return 'What is the difference of {} - {}?'.format(A, B), answer
    elif sign == 2:
        answer = A * B
        return 'What is the product of {} x {}?'.format(A, B), answer
    else:
        answer = round(A / B, 1)
        return 'What is the quotient of {} {} {} to the nearest 10th?'.format(A, chr(247), B), answer

def checkSolution(user_text, solution, cheatAns):

    try:
        if cheatAns: # Check if cheat code is enabled
            # check the answer, plus the cheat code
            if float(user_text) == cheatAns or float(user_text) == solution:
                return True
            else:
                return False
        elif float(user_text) == solution: # check the answer
            return True
        else:
            return False
    except:
        # In the event converting user_text to a float fails
        # (for example if its not numbers) parse out the problematic
        # characters.
        if user_text == "":
            return 'Error: Please enter your answer in the box!'
        junk = ''
        for character in user_text:
            if not character.isdigit():
                #user_text.replace(character, '') Future project to try and sanitize non-digit characters
                junk += ("'" + character + "' ")
        print('Error: Numbers only please!\n{}are/is not valid!'.format(junk))
        return False