"""
Q1. 2  22  222  2222  22222 ... upto n. (Ask n from user)
"""

def pattern(n:int):
    i = 1
    while i<=n:
        print(i*str(2), end=' ')
        i+=1
n = int(input("Enter the number = "))
pattern(n)















