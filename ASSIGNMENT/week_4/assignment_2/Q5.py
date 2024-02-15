"""
Q5. Count how many numbers are divisible by 3 and 6 between 1 to 1000 by using list comprehension.
"""

def count_(num):
    count=0
    if num:
        count+=1
    return count

lst = [count_(i) for i in range(1,1000+1) if i%3==0 and i%6==0]
print(len(lst))

# method 2nd
print(len([i for i in range(1, 1001) if i % 3 == 0 and i % 6 == 0]))