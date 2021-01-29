import random
from practice_problems import (
    roman_numeral_converter,
    square_every_digit,

)

catalog = [
    roman_numeral_converter,
    square_every_digit,

]


def get_random():
    problem = random.choice(catalog)
    return problem.response_class


def search(criteria):
    pass