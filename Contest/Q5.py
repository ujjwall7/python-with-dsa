"""
Q5. Make a function named sumOfFirstAndLastDigit which accepts an
integer n from the user. Calculate the sum of first and last digit of a
number and return it.
"""


def sumOfFirstAndLastDigit(num:int):
    i=1
    num=str(num)
    first_index = num[0:1]
    last_index = num[:-2:-1]
    print(f"{first_index = }")
    print(f"{last_index = }")
    return int(first_index) + int(last_index)

print(sumOfFirstAndLastDigit(21234465))





