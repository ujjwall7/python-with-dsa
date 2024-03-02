"""
Q3. Write a function which accepts a String as a parameter and return the reversed words as a String.
"""


def reverseWords(string:str):
    get_str = string.split(' ')
    get_str.reverse()
    res = " ".join(i for i in get_str)
    return res


print(reverseWords('python is greeet'))






