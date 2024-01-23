"""
Enter a number = 10
Enter a number = 15
Enter a number = 12

total = 22
"""

def cal():
    count = 0
    while True:
        number = int(input("Enter the nmber = "))
        count+=number
        if number==0:
            return count
            break
print(cal())

















