"""
Q5. Create a Python function to sort a dictionary by its values. And return that new dictionary.
"""

def sortDictionary(_new_dict:dict):
    _new = sorted(_new_dict.items(), key= (lambda x:x[1]))
    return _new



x = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}

obj = sortDictionary(x)
print(obj)
