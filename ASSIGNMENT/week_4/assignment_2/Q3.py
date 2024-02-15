"""
Q3. Write a Python program to generate a list of prime numbers less than 500 using list comprehension.
Example output: [2, 3, 5, 7, 11, 13, 17, 19, 23, ..., 491, 499]
500 can be changed to anything.
"""

def prime(num:int):
    count = 0
    for i in range(1, num+1):
        if num%i==0:
            count+=1
        else:
            pass
    if count==2:
        return num
    else:
        return None
    

lst = [prime(i) for i in range(1, 500+1) if prime(i) is not None]
print(lst)













