"""
Q6. Write a Python program to find the maximum and minimum value in a dictionary.
"""


def maximum_(_dict):
    maxi = _dict["One"]
    # print(maxi)
    for key, val in _dict.items():
        # print(f"{key} = {val}")
        if maxi < val:
            maxi = val
        else:
            pass
    return maxi

def minimum_(_dict):
    maxi = _dict["One"]
    # print(maxi)
    for key, val in _dict.items():
        # print(f"{key} = {val}")
        if maxi > val:
            maxi = val
        else:
            pass
    return maxi

def checkMaxAndMin(a):
    maximum = maximum_(a)
    minimum = minimum_(a)
    return f"Maximum = {maximum}\nMinimum = {minimum}"


x = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}

obj = checkMaxAndMin(x)
print(obj)




