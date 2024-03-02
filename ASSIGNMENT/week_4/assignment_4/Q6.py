"""
Q6. Write a function which accepts a String and another string (which will be a single character) as a parameter. 
Join that string along with that character.
"""


def joinString(string_1:str, string_2:str):
    new = f"{string_2}".join(i for i in string_1.split(' '))
    return new
    
    

print(joinString('megha sharma hello world new update', 'YES'))




