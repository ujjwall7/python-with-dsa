"""
Q5. Write a program to put all the common elements (in 2 lists) in another list and print it using function.
"""


def commonElements(lst1: list[int], lst2: list[int]):
    new_list = []
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i] == lst2[j]:
                if lst1[i] not in new_list:
                    new_list.append(lst1[i])
    return new_list


l1 = [1, 25, 5, 4, 58, 5, 54, 5, 4, 514, 1]
l2 = [1, 54, 5, 4, 514, 1, 23, 453]
print(commonElements(l1,l2))
