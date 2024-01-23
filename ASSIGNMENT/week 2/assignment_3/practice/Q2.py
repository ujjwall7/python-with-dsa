"""
factors.py
"""


def factorial_numbers(a: int):
    num = 1
    factorial = 1
    while num <= a:
        factorial *= num
        num += 1
    return factorial


print(factorial_numbers(5))