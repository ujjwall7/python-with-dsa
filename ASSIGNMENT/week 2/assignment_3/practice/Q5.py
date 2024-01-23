"""
n1=30
n2=6

1 to n1 (1 to 30)
divisible by n2

calculate total
"""


def divisible(n1:int, n2:int):
    i=1
    count = 0
    while i<=n1:
        if i%n2==0:
            # print(i)
            count += i
        i+=1
    return count

print(divisible(30,7))











