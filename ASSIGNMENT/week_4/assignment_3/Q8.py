"""
Q8. Ask a string from user. Print the string with first 2 letters and last 2 letters.
Example string: aeroplane
Output: aene
If length is less than 3, print “INVALID”
"""


def twoWords(string=str):
    if len(string) <= 3:
        print("Invalid String")
    else:
        first_two_char = string[:2]
        last_two_char = string[-2::1]
        print(first_two_char + last_two_char)

a=input("enter the string = ")
twoWords(a)
