import random


def roll():
    result = random.randint(1, 6)
    return result >= 5
