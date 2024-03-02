"""
Q1. Ask a string from user. If the length of string is odd, 
then change all the capital letters to small and vice versa, 
but if the length of string is even, reverse the string. 
Do this using a function and return the output.
"""

def reverse_str(string:str):
    new_str = ''
    for i in range(len(string)-1,-1,-1):
        new_str+=string[i]
    return new_str

def stringOddEven(string:str):
    length = len(string)
    if length%2==0:
        get__reverse = reverse_str(string)
        new = get__reverse.lower()
    else:
        new = string.upper()
    return new

print(stringOddEven("Megha Sharma"))










