"""
Q5. Write a function which accepts a String as a parameter and return each word being in reverse.
"""

def reverse_str(string:str):
    print(len(string))
    new_str = ''
    for i in range(len(string)-1,-1,-1):
        print(i)
        new_str+=string[i]
    return new_str

print(reverse_str('megha sharma'))


