"""
Q5. Create a function addDigits() that takes an integer as an argument.
Calculate the sum of digits of that number.
"""


def addDigits(n: int):
    num: int = n
    count = 0
    while num > 0:
        count += num % 10
        num = num // 10
    return count


user = int(input("Enter the number = "))
obj = addDigits(n=user)
print(obj)
