"""
ask a number from a user 
print yes - is it divisible by 5 and 6  else NO
"""


num: int = int(input("Enter the number = "))

if num % 5 == 0 and num % 6 == 0:
    print("YES")
else:
    print("NO")




    