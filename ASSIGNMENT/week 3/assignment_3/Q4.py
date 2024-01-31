"""
Q4. Create a function findSmallest that accepts an List of Integers and returns the smallest number from the list.
"""
from typing import List


def findSmallest(lst:List[int]):
    smallest = lst[0]
    for i in range(len(lst)):
        if smallest<=lst[i]:
            continue
        else:
            smallest = lst[i]
    return smallest


my_list = [
    34,
    11,
    91,
    59,
    33,
    22,
    1004,
    -1,
    0,
    -12,
]

print(findSmallest(my_list))













