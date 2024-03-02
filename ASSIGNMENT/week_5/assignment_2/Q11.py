"""
Write a Python function that takes a dictionary as input where the values are lists. 
The function should return a new list containing all the elements from all the lists in the dictionary.
It should have at least 3-4 keys and any amount of elements can be in a list.

input = {
'A':[1,2,3],
'B':[4,5,6]
}
output = [1,2,3,4,5,6]
"""

def dictionaryFunction(marks:dict):
    new = []
    for key, value in marks.items():
        for i in value:
            new.append(i)
    return new

input = {
'A':[1,2,3],
'B':[4,5,6]
}
obj = dictionaryFunction(marks=input)
print(obj)









