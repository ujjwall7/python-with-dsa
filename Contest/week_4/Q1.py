"""
Q1. Create a python function named isPalindrome which accepts a string 
as a parameter and return True if its a palindrome. 
Palindrome are words which is same when read from start and same when read from the end.
"""

def reverse(string:str):
    new_=''
    for i in range(len(string)-1,-1,-1):
        new_ = new_+ string[i]
    return new_

def isPalindrome(string:str):
    if string==reverse(string):
        print(True)
    else:
        print(False)

isPalindrome('nitin')


