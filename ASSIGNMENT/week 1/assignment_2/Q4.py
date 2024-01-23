"""
Q4. Write a Python program that takes a student's score as input and prints the corresponding grade. Use the following grading scale:
A: 90-100
B: 80-89
C: 70-79
D: 60-69
E: Below 60
"""
num :int = int(input("Enter the number = "))

if num >=90 and num<=100:
    print("A GRADE")
elif num >=80 and num<=89:
    print("B GRADE")
elif num >=70 and num<=79:
    print("C GRADE")
elif num >=60 and num<=69:
    print("B GRADE")
elif num<=60:
    print("E GRADE")
else:
    print("Invalid")


