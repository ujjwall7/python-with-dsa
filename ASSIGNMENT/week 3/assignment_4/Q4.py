"""
Q4. Write a Python Program to find sum and average of List in Python.
"""


def sumAverage(lst: list[int]):
    count = 0
    for i in range(len(lst)):
        count += int(lst[i])
    return (count / len(lst))


l1 = ([1, 25, 5, 4, 58, 5, 54, 5, 4, 514, 1])
print(sumAverage(l1))