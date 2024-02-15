"""
Q1. Write a Python code to check if a given list is sorted in ascending order.
You don’t have to change the list. Just output YES if list is sorted else NO.
"""

my_list=[1,2,3,4,5,6,743,23,234,324,324,32,123,221]
my_list=[1,2,3,4,5,6]
not_found = False
for i in range(len(my_list)-1):
    # print(my_list[i], end=" ")
    if my_list[i]<my_list[i+1]+1:
        pass
    else:
        print("No")
        not_found = True
        break
if not_found==False:
    print("YES")
        









