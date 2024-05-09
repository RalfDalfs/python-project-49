from random import randint

LOWER_LIMIT = 1
UPPER_LIMIT = 100
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_round_data():
    progression_len = randint(5, 10)
    progression_step = randint(1, 10)
    progression = []
    progression.append(str(randint(LOWER_LIMIT, UPPER_LIMIT)))
    for i in range(progression_len):
        progression.append(str(int(progression[i]) + progression_step))
    random_index = randint(0, progression_len - 1)
    correct_answer = progression[random_index]
    progression[random_index] = '..'
    return " ".join(progression), correct_answer
