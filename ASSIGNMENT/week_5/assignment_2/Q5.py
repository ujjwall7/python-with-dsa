"""
Q5. Write a Python program to combine two dictionary by adding values for 
common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: {'a': 400, 'b': 400, 'd': 400, 'c': 300}
"""

def combineDictionary(d1:dict, d2:dict)->dict:
    merged = {}
    for key, value in d1.items():
        if key in d2:
            # print(key)
            merged[key] = int(d1[key]) + int(d2[key])
        elif not key in d2:
            merged[key] = int(d1[key])
    for key, value in d2.items():
        if not key in merged:
            merged[key] = int(d2[key])
    return merged


d1 = {'a': 500, 'b': 200, 'c':300,'h':893}
d2 = {'a': 300, 'b': 200, 'd':400}
obj = combineDictionary(d1,d2)
print(obj)