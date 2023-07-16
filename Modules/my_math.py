import math

CONSTANT = 1337


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return math.inf

    return a / b


print(f"my_math.py: {__name__}")