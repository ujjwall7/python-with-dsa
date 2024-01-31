"""
Q5. Create a function updateOddEven that accepts an List of Integers and 

update all the even numbers to 0 
and 
update all the odd numbers to 1.
"""

def updateOddEven(lst:list[int]):
    for i in range(len(lst)):
        if lst[i]%2==0:
            lst[i]=0
        else:
            lst[i]=1
    return lst

my_list = [
    34,
    11,
    91,
    59,
    33,
    22,
    1004,
    -1,
    0,
    -12,
]

print(updateOddEven(my_list))
















