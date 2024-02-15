"""
Q7. Make two lists of same length and pass it to a function. Return a third list where each element is the sum of index.
"""


def addTwoListElements(lst1: list[int], lst2: list[int]):
    if not len(lst1) == len(lst2):
        return "List size not equal!"
    new_list = []
    for i in range(len(lst1)):
        new = lst1[i] + lst2[i]
        new_list.append(new)
    return new_list


l1 = [1, 25, 5, 4, 58, 5, 54, 5, 4]
l2 = [1, 54, 5, 4, 514, 1, 23, 453, 4]
print(addTwoListElements(l1, l2))
