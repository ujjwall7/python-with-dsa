"""
Q2. Write a Python program to generate a list of factorials less than 1000
using list comprehension.
Example output: [1, 2, 6, 24, 120, 720]
1000 can be changed to anything.
"""

def factorial(num:int):
    fact = 1
    for i in range(1,num+1):
        fact*=i
    return fact



inp = int(input("Enter the number = "))
fact=1
a = [factorial(i) for i in range(1,inp+1) if factorial(i) <= 1000]
print(a)

