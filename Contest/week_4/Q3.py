"""
Q3. Python Program to remove all duplicates from a given string.
"""


def removeDuplicates(string:str):
    new = ''
    for i in range(len(string)):
        if not string[i] in new:
            new += string[i]
    return new


x = removeDuplicates('ujjwal sharma')
print(x) 









