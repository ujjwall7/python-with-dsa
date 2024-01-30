"""
Q3. Create a function named as printPrimeFactors that takes an integer n as a 
argument and print all the prime factors of that number.
"""

def checkPrime(n:int):
    i=1
    count=0
    while i<=n:
        if n%i==0:
            count+=1
        i+=1

    if count==2:
        return True
    else:
        return False


def printPrimeFactors(n:int):
    i=1
    while i<=n:
        # print(f"{i},", end=' ')
        if n%i==0:
            if checkPrime(i):
                print(f"{i},", end=' ')
        i+=1
    print()

printPrimeFactors(20)
printPrimeFactors(7)
printPrimeFactors(72)










