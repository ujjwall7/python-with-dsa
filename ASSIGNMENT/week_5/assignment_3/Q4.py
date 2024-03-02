"""
Q4. Write a Python program to Convert two lists into a dictionary
Sample Output
keys = ["One", "Two", "Three", "Four", "Five"]values = [1, 2, 3, 4, 5]
"""

def converdict(key:list, value:list):
    _new = {}
    for i in range(len(key)):
        for j in range(i,i+1):
            _new[key[i]] = value[j]
    return _new


keys = ["One", "Two", "Three", "Four", "Five"]
values = [1, 2, 3, 4, 5]
x = converdict(keys, values)
print(x)


