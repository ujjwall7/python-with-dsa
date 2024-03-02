"""
Q6. Make a password strength function. It will accept a string from user.
Return True if it is a strong password.Strong password has these characteristics.
Minimum 8 character
Minimum 1 uppercase alphabet
Minimum 1 lowercase alphabet
Contains at least 1 special symbol (any symbol)
Minimum 1 digit
"""

def stringCheck(string:str):
    if not 8<=len(string):
        print("String should be mininum 8 length")
    upper = False
    lower = False
    symbol = False
    digit = False
    for i in string:
        if i.isupper():
            upper = True
            print(f"{upper = }")
        elif i.islower():
            lower = True
            print(f"{lower = }")
        elif i.isalnum:
            symbol= True
            print(f"{symbol = }")
        elif not i.isdigit():
            digit = True
            print(f"{digit = }")
    
    if upper==True and lower==True and symbol==True and digit==True:
        print(True)
    else:
        print(False)

stringCheck("Python1$")











