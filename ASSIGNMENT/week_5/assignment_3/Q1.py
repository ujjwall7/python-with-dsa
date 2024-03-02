"""
NOTE:
Q1. Write a Python script to sort (ascending and descending) a dictionary by value.
Sample Outputdictionary = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
Ascending order = { 0:0, 2:1, 1: 2, 3: 4}Descending order = {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}
"""

def sortDict(sample:dict):
    ls = sample.items()
    print(ls)
    ass = sorted(ls, key = lambda x:x[1])
    desc = sorted(ls, key = lambda x:x[1], reverse=True)
    return f"ascending = {ass} \ndescending = {desc}"

    
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(sortDict(x))

