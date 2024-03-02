"""
Q4. Write a Python function that takes two dictionaries as input, 
where the values are lists. 
The function should merge the lists corresponding to the same keys in both dictionaries into a 
single list and return a new dictionary with these merged lists.
"""

from typing import Dict
def mergeDictionary(dict1:dict, dict2:dict)->Dict:
    pass



dict1 = {"x": [1, 2, 3], "y": [4, 5, 6]}
dict2 = {"x": [7, 8, 9], "y": [10, 11, 12], "z": [99, 100, 111]}
result = mergeDictionary(dict1, dict2)
print(result)



