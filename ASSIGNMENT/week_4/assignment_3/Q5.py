"""
Q5. Write a Python program to check if a string has at least one letter and one number. 
If it has at least one letter and one number then print YES else print NO.
"""


def checkStringOrInt(string: str):
    isLetter = False
    isDigit = False

    for i in string:
        if i.isdigit():
            isDigit = True
        elif i.isalpha():
            isLetter=True
    return isLetter and isDigit

print(checkStringOrInt("eerj54"))
