import random


def roll():
    result = random.randint(1, 6)
    print(f">> Dice throw result: {result}")
    return result >= 5
