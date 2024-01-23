"""
Q1. Create a function named factorial which takes a integer as an input and
returns the factorial of that number.
Factorial of 5 means 5 x 4 x 3 x 2 x 1 = 120
"""


def factorial_numbers(a: int):
    num = 1
    factorial = 1
    while num <= a:
        factorial *= num
        num += 1
    return factorial


print(factorial_numbers(5))
