"""
Q9. Write a python program to only print second half of the string. Ask string from user.
Example string: aeroplane
Output: lane
"""

def printSecond(string:str):
    new_len = len(string)//2
    new = len(string) - new_len
    print(string[new:])

a = input("Enter the string = ")
printSecond(a)


# a = str("happy")
# b = eval("'happy'")
# print(type(a))
# print(type(b))
