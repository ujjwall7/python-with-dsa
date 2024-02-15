"""
Q3. Write a Python program to check whether an element exists within a
tuple. Ask something from user, if that exists in tuple, then print “YES” else
print “NO”.
"""

def checkElementExists(tup:tuple):
    num = int(input("Enter The Number = "))
    if num in tup:
        print("YES")
    else:
        print("NO")

a = ("1", 12, "ujjwal", "*", 55, 85, 87, 98, "ujjwal")
checkElementExists(tup=a)









