"""
Q2. Write a function to remove duplicates from a list and print them.
"""

from typing import List


def removeDuplicates(lst: List[int]):
    unique_list = []
    for i in range(len(lst)):
        if lst[i] not in unique_list:
            unique_list.append(lst[i])
    return unique_list


print(
    removeDuplicates(
        [
            1,
            24,
            2,
            13,
            12,
            31,
            353,
            353,
            1,
            2,
            1,
            44,
            44,
            85,
            96,
            85,
            96,
        ]
    )
)
