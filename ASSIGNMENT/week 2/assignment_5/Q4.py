"""
Ask x and n from user and then calculate the following answer.
"""


def pattern(x:int, n:int):
    count = 1
    i =1
    calculation = 0
    while count<=n:
        if count==n:
            if count%2==0:
                calculation += x**i
                print(f"{x}^{i} = {calculation}", end='')
                count+=1
                break
            else:
                calculation -= x**i
                print(f"{x}^{i} = {calculation}", end='')
                count+=1
                break

        if count%2==0:
            calculation += x**i
            print(f"{x}^{i} + ", end='')
            count+=1
        else:
            calculation -= x**i
            print(f"{x}^{i} - ", end='')
            count+=1
        
        i+=2

x_var = int(input("Enter the value of x = "))
n_var = int(input("Enter the value of n = "))
pattern(x=x_var, n=n_var)










