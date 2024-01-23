"""
Q1. Write a program to print absolute vlaue of a number entered by user.
Example 1
Input = -18
Output = 18
Example 2
Input = 9
Output = 9
"""


num: int = int(input("Enter the number : "))
if num < 0:
    print(num * -1)
else:
    print(num)




