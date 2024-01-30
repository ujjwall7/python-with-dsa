"""
Create a function named as checkPrime that takes an integer as an
argument. Print YES if the number passed is a prime number else print NO.
"""

count = 0


def primeFactors(num: int):
    new = ""
    i = 1
    while i <= num:
        if num % i == 0:
            global count
            count += 1
            new = new + str(i) + str(" ")
        i += 1
    return new


number = int(input("Enter the number = "))
primeFactors(number)
if count == 2:
    print("Prime")
    print(primeFactors(number), end=" ")
else:
    print("Not Prime")
