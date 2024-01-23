"""
Q1. Create a function named div_by_3_and_5 which takes 2 integers as a arguments (n1,n2), 
and print all the numbers divisible by 3 and 5 between n1 and n2.
"""

def div_by_3_and_5(n1: int, n2: int) -> int:
    while n1 <= n2:
        if n1 % 3 == 0 and n1 % 5 == 0 and n2 % 3 == 0 and n2 % 5 == 0:
            print(n1, end= ' ')
            n1 += 1
        else:
            n1 += 1
    
div_by_3_and_5(10,30)
print()
print('--------------------------------')
div_by_3_and_5(1,60)

