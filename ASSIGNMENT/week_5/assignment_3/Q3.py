"""
Q3. Write a Python program to print a dictionary line by line.
Sample Output
Dict = {  
    "Sam" : {"M1" : 89, "M2" : 56, "M3" : 89}, 
    "Suresh" : {"M1" : 49, "M2" : 96, "M3" : 89} 
    }
Sam
M1 : 89
M2 : 56
M3 : 89

Suresh
M1 : 49
M2 : 96
M3 : 89
"""

def printNames(new_dict : dict):
    print(f"{new_dict = }\n")
    for key, val in new_dict.items():
        print(f"{key}")
        for i in val:
            print(i)
        print()



x = {  
    "Sam" : {"M1" : 89, "M2" : 56, "M3" : 89}, 
    "Suresh" : {"M1" : 49, "M2" : 96, "M3" : 89} 
    }
obj = printNames(x)

# print(obj)
