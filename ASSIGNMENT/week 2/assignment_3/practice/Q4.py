def checkPrime(num:int):
    i = 1
    count= 0
    while i<=num:
        if num%i==0:
            count +=1
        i+=1
    
    if count==2:
        print('Prime')
    else:
        print("not prime")

checkPrime(3)












