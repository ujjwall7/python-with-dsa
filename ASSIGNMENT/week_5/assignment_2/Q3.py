"""
Q3. Write a Python function that takes a dictionary as input where the values are lists of integers.
The function should return a new dictionary where the values are lists containing only the even 
integers from the original lists.
"""
from typing import Dict

def filterEvenIntegers(dictionary: Dict) -> Dict:
    for key, value in dictionary.items():
        even_list = []
        for i in value:
            if i%2==0:
                even_list.append(i)
        dictionary[key] = even_list
    return dictionary


inp = {
'A':[1,2,3,43,14],
'B':[4,5,6,12]
}
print(filterEvenIntegers(inp))



