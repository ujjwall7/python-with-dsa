"""
Q7. Create a Python program to find the dierence between two dictionaries.
First dictionary: {'a': 1, 'b': 2, 'c': 3}Second dictionary: {'b': 2, 'c': 4, 'd': 5}OUTPUT:
Keys present only in the first dictionary: ['a']Keys present only in the second dictionary: ['d']
Keys present in both dictionaries: [’b’, ‘c’
"""

def checkDictionary(a:dict, b:dict):
    first_dictionary = []
    second_dictionary = []
    for i in a:
        # print(i)
        if not i in b:
            # print(i)
            first_dictionary.append(i)
        elif i in b:
            second_dictionary.append(i)
    return f"first_dictionary = {first_dictionary}\nsecond_dictionary = {second_dictionary}"


x = {'a': 1, 'b': 2, 'c': 3}
y = {'b': 2, 'c': 4, 'd': 5}

obj = checkDictionary(x, y)
print(obj)





