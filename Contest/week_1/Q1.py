"""
Q1. Make a function named reverse which accepts an integer n from the
user. Reverse the number passed as a parameter and return the reverse
number. Do not use STRINGS.
"""

def reverse(num:int):
    n :int = num
    reverse = 0
    while n>0:
        reminder = n%10
        reverse = reverse*10 + reminder
        n = n//10
    return reverse

print(reverse(562))













