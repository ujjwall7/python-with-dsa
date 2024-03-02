"""
Q7. Write a function which accepts a String and another string (which will be a single character) as a parameter.
Join that string along with that character but in reverse.
"""


def string(string:str):
    new = string.split(' ')
    print(new)
    _new=" ".join(new[i] for i in range(len(new)-1,-1,-1))
    print(_new)


string("Hello megha sharma i love u")








