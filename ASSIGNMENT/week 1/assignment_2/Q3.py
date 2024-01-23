"""
Q3. Write a program to check if number is divisible by 2 and 3 but not 8
"""

num: int = int(input("Enter the number = "))

if num % 2 == 0 and num % 3 == 0 and (not (num % 8 == 0)):
    print(f"{num} is divisible by 2 and 3 but not 8")
else:
    print(f"{num} is  NOT DIVISIBLE by 2 and 3 but not 8")