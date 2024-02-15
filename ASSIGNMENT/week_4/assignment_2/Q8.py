"""
Q8. Write a python program which prints all the values whose count is greater than 3. 
(Make sure to make a list with at least 15 numbers)Store them in another list using list comprehension
"""

def countCheck(num:int,lst:list):
    new=[]
    for i in range(len(lst)):
        if lst.count(lst[i])>3:
            if lst[i] not in new:
                new.append(lst[i])
    return new


my_list = [1,2,3,4,1,1,1,2,2,2,5,54154,1,2,456,74,57,21,52,7,1,5,47,1,54,74,58,77,87,55,4,52,52,52,52]
a =[i for i in range]


my_list.count(52)
print(countCheck(1,my_list))










