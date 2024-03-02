"""
Q4. Ask 5 integers from user. 
Then ask a single character from user. 
Print those integers separated by that character entered by user.
"""

def program():
    str_l = []
    for i in range(5):
        new = input('Enter the number = ')
        str_l.append(new)
    _new = input('Enter the chracter = ')
    get = f"{_new}".join(i for i in str_l)
    return get

print(program())













