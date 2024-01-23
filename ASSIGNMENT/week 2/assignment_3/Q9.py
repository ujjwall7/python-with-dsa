"""
Q4. Don’t create a function, just print the following pattern
1 11 111 1111 11111....n times (Ask n from user)
"""

def print_num(num:int):
    i = 1
    str = "1"
    while i<=num:
        print(i*str, end=' ')
        i+=1

print_num(5)




