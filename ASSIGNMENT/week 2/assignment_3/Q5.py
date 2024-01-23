"""
Q5. Create a function named printPattern that takes one integer (num) as an argument.
Print from -num to num. Also keep in mind number passed as an argument can be negative or positive.
"""

def printPattern(num):
    if num>0:
        num_negative = num//-1
        num_positive = int(num)
        while num_negative<=num_positive:
            print(f"{num_negative}", end=' ')
            num_negative+=1
    if num<0:
        num_negative = num
        num_positive = num*-1
        while num_negative<=num_positive:
            print(f"{num_negative}", end=' ')
            num_negative+=1

printPattern(5)
print()
print('---------------------')
printPattern(-9)

#----------New Method---------------
def printPattern(num: int):
    if num > 0:
        start: int = -num
        end: int = num
    else:
        start: int = num
        end: int = -num
    while start <= end:
        print(start, end=" ")
        start += 1
    print()


printPattern(-9)











