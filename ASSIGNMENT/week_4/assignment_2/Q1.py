# Q1. Write a Python program to generate a list of powers of 2 less than 100
# using list comprehension.
# Example output: [1, 2, 4, 8, 16, 32, 64]
# 100 can be changed to anything.
inp = int(input("Enter the number = "))
a = [i**2 for i in range(1, inp + 1) if i**2<=100]
print(a)