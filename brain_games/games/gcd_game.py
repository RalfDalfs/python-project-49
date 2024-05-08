from random import randint

LOWER_LIMIT = 1
UPPER_LIMIT = 100
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_round_data():
    num_1 = randint(LOWER_LIMIT, UPPER_LIMIT)
    num_2 = randint(LOWER_LIMIT, UPPER_LIMIT)
    correct_answer = str(gcd_fun(num_1, num_2))
    random_number = f'{num_1, num_2}'
    return random_number, correct_answer


def gcd_fun(num_1, num_2):
    if num_2 == 0:
        return num_1
    else:
        return gcd_fun(num_2, num_1 % num_2)
