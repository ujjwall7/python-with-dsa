# """
# Q7. Create a function calculatePrime that accepts an List of Integers and print all the prime numbers in that list.
# """

def checkPrime(number:int=None):
    count = 0
    if number:
        for i in range(1,number+1):
            if number%i==0:
                count+=1
            else:
                pass
        if count==2:
            return True
        else:
            return False
    else:
        print("Not Found!")

def calculatePrime(lst: list[int]):
    for i in range(len(lst)):
        check=checkPrime(lst[i])
        if check is True:
            print(lst[i], end=' ')
        else:
            pass

my_list = [34, 11, 91, 59, 33, 22, 1004, 2,5]

calculatePrime(my_list)
