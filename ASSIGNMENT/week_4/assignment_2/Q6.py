"""
Q6. Remove duplicates from the list just by using list comprehension.
"""

lst = [1,21,32,132,123,1,12,435,3,2242,13,42,133,2332,1,3,5,3,22,12,454,56,7,66,5,65,54]
result = []
a = [result.append(lst[i]) for i in range(len(lst)) if not lst[i] in result]
print(result)










