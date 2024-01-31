"""
Q1. Create a function countOddEven that accepts an List of Integers and print how many even and odd numbers are there.
"""

from typing import List


def countOddEven(lst: list[int]):
    odd_count = 0
    even_count = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    get_odd_count = f"Total Odd Numbers {odd_count}"
    get_even_count = f"Total Even Numbers {even_count}"
    return get_odd_count, get_even_count

my_list = [
    34,
    11,
    91,
    59,
    33,
    22,
]
print(countOddEven(my_list))


