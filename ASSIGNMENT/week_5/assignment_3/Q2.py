"""
Q2. Write a Python program to count number of items in a dictionary value that is a list.
Sample Output
Dict = { 
    'M1' : [67, 79, 90, 73, 36], 
    'M2' : [89, 67, 84], 'M3' : [82, 57] 
    }
    Number of Items in a Dictionary : 10
"""

def countValue(new_dict:dict):
    count = 0
    print(f"{new_dict = }\n")
    for key, val in new_dict.items():
        # print(f"{key} = {val}")
        for i in val:
            # print(f"{i}")
            count+=1
    return count


Dict = { 
    'M1' : [67, 79, 90, 73, 36], 
    'M2' : [89, 67, 84], 'M3' : [82, 57, 12] 
    }
x = countValue(Dict)
print(x)







