"""
Q4. Make a function named checkArmstrong which accepts an integer n
from the user. Return True or False if that number is an armstrong number.

153
407
"""

def armstng(num):
    num_str = str(num)
    length_number = len(num_str)
    _sum = 0
    for i in num_str:
        _sum += int(i)**length_number
    
    if _sum==num:
        return True
    else:
        return False

print(armstng(153))
 


