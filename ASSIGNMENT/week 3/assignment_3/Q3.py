"""
Q3. Create a function findLargest that accepts an List of Integers and returns the largest number from the list.
"""

from typing import List

def findLargest(lst:List[int]):
    largest = lst[0]
    for x in range(len(lst)):
        if largest<=lst[x]:
            largest = lst[x]
        else:
            continue
    return largest


my_list = [
    34,
    11,
    91,
    59,
    33,
    22,
    1004,
]

print(findLargest(my_list))















