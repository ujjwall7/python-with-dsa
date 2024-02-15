"""
Q6. Write a program to remove the nth index element from a list using a function. 
"""


def removeElements(lst1: list[int], index=int):
    if len(lst1) <= index:
        return "Index does not exists!"
    else:
        del lst1[index]
        return lst1


l1 = [1, 54, 5, 4, 514, 1, 23, 453]
print(removeElements(l1, 3))
