"""
Q7. Make two lists of same length and pass it to a function.
Return a third list where each element is the sum of index. 
Use List Comprehension
"""

l1 = [1, 25, 5, 4, 58, 5, 54, 5, 4]
l2 = [1, 54, 5, 4, 514, 1, 23, 453, 4]
new_list = []

a = [l1[i] + l2[i] for i in range(len(l1))]
print(a)











