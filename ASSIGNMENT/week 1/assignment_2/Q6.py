"""
Q6. Ask 4 numbers from user. 
Make sure all the numbers entered by user are diffrent. 
Print which number is the smallest.
"""

num_1: int = int(input("Enter the 1st number = "))
num_2: int = int(input("Enter the 2nd number = "))
num_3: int = int(input("Enter the 3rd number = "))
num_4: int = int(input("Enter the 4th number = "))

smallest = num_1

if num_2 < smallest:
    smallest = num_2
if num_3 < smallest:
    smallest = num_3
if num_4 < smallest:
    smallest = num_4
print(f"The smallest number is {smallest}")
