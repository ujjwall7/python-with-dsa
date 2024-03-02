"""
Q2. Create a function named countChar which will accept a string as a parameter. 
Create a dictionary having frequency of each character.
"""

def countChar(sentence:str):
    new = {}
    for i in sentence:
        if i in new:
            new[i] += 1
        else:
            new[i] = 1
    return new

obj = countChar("Megha Sharma ujjwal Sharma")
print(obj)



