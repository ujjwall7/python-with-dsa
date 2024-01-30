"""
Q2. Create a function named as checkPrime that takes an integer as an argument. 
Print YES if the number passed is a prime number else print NO.
"""


def checkPrime(n: input):
    count = 0
    i = 1
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    if count ==2:
        print("Yes")
    else:
        print("No")

checkPrime(7)
