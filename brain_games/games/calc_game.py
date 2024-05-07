from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 100
DESCRIPTION = 'What is the result of the expression?'


def get_round_data():
    random_number_1 = randint(LOWER_LIMIT, UPPER_LIMIT)
    random_number_2 = randint(LOWER_LIMIT, UPPER_LIMIT)
    random_number = f'{random_number_1} + {random_number_2}'
    correct_answer = str(random_number_1 + random_number_2)
    return random_number, correct_answer
