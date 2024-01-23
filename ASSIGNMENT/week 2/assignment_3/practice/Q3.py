def printFactors(num: int):
    i=1
    while i<=num:
        if num%i==0:
            print(i,end=' ')
        i+=1

def countFactors(num:int):
    i=1
    count=0
    while i<=num:
        if num%i==0:
           count+=1 
        i+=1
    return count

printFactors(14)
print()
print('-------------')
print(countFactors(14))



