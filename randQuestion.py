from os import chdir
import random

def question():
    sign = random.randint(0, 3)
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
