"""
Q3. Write a Python function that takes two lists and returns True if they have at least one common element.
"""

from typing import List


def twoList(l1: List[int], l2: List[int]):
    found = False
    for x in range(len(l1)):
        if l1[x] in l2:
            found = True
    if found == True:
        return True
    else:
        return False


print(
    twoList(
        l1=[1, 25, 5, 4, 58, 5, 54, 5, 4, 514, 1],
        l2=[845, 74845, 84, 84, 84, 854, 84185, 1, 541, 7845],
    )
)
