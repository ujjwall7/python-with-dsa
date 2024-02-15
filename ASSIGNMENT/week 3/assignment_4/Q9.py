"""
Q9. Make a list. Write a simple program for addition of the 2nd element from start to 2nd element from the end.
"""


def addition(my_lst: list[int]):
    ad = 0
    for i in range(1, len(my_lst) - 1):
        print(my_lst[i], end=" ")
        ad += my_lst[i]
    print()
    print()
    return ad


print(addition(my_lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
