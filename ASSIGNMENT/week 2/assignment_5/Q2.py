"""
Q2. Write a program to display the n terms of a harmonic series and their 
sum. 1 + 1/2 + 1/3 + 1/4 + 1/5 ... 1/n termsLets suppose n=5.
1/1 + 1/2 + 1/3 + 1/4 + 1/5 = 2.283334
"""

def pattern(n:int):
    i=1
    number = 1
    count = 0
    while i<=n:
        count+=1/i
        if i==n:
            print(f"1/{n} = {count}", end = '')
            break
        print(f'1/{i} + ', end = '')
        i+=1
n = int(input("Enter the number = "))
pattern(n)













