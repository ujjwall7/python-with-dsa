"""
Q2. Write a Python program to find repeated items in a tuple.
"""


def checkDuplicate(tup: tuple, num: int | str):
    count = 0
    for i in tup:
        if i == num:
            count += 1
    if 1 < count:
        return True
    else:
        return False

def findRepeated(tup: tuple):
    for i in range(len(tup)):
        check = checkDuplicate(tup, tup[i])
        if check == True:
            print(tup[i], end=" ")
    if check == False:
        print("No duplicates")


x = ("1", 12, "ujjwal", "*", 55, 85, 87, 98, "ujjwal")
findRepeated(x)
