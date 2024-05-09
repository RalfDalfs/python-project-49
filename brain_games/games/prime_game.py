from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 100
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_round_data():
    question = randint(LOWER_LIMIT, UPPER_LIMIT)
    if is_prime(question) == True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def is_prime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n
