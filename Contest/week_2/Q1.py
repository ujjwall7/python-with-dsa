"""
Q1. Make a function named sumPattern that takes an integer n as an
argument from the user. And then calculate the sum of the following
pattern.

sumPattern(5)
1/1! + 1/2! + 1/3! + 1/4! + 1/5! =  1.71
"""


def factorial(n: int):
    i = 1
    cal = 1
    while i <= n:
        cal *= i
        i += 1
    return cal

def sumPattern(n: int):
    calcultion = 0
    i = 1
    while i <= n:
        if i == n:
            calcultion += (1 / factorial(i))
            print(f"1/{i}! = {calcultion}", end="")
            # print(f"1/{i}! = {1/factorial(i)}")
            break
        print(f"1/{i}! + ", end="")
        calcultion += (1 / factorial(i))
        # print(f"1/{i}! = {1/factorial(i)}")
        
        i += 1


number = int(input("Enter the number = "))
sumPattern(n=number)
# print(factorial(5))
