from random import randint
from random import choice

LOWER_LIMIT = 0
UPPER_LIMIT = 100
DESCRIPTION = 'What is the result of the expression?'


def get_round_data():
    operator = choice(['*', '-', '+'])
    random_number_1 = randint(LOWER_LIMIT, UPPER_LIMIT)
    random_number_2 = randint(LOWER_LIMIT, UPPER_LIMIT)
    random_number = f'{random_number_1} {operator} {random_number_2}'
    correct_answer = str(calculate(random_number_1, random_number_2, operator))
    return random_number, correct_answer


def calculate(num_1, num_2, operator):
    if operator == '*':
        return num_1 * num_2
    elif operator == '-':
        return num_1 - num_2
    else:
        return num_1 + num_2
