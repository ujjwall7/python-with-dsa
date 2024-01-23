"""
Q4. Create a function named calSum which takes an 2 integer (n1 and n2) 
as an argument. Calculate the sum of all the numbers divisible by 5 
between n1 and n2 and return that sum. (Make sure that n1 is less than n2).
"""


def calSum(n1: int, n2: int):
    if n1>n2:
        return 'n1 is smaller than n2'
    count = 0
    while n1 <= n2:
        if n1 % 5 == 0:
            count += n1
            n1 += 1
        else:
            n1 += 1
    return count

print(calSum(1,10))
print('--------------------')
print(calSum(43,68))
