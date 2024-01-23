"""
Ask a mark from user
91 - 100 -> A
81 - 90 -> B
71 - 80 -> C
1 - 70 -> Fail
"""

marks: int = int(input("Enter the marks = "))

if marks <= 100 and marks >= 91:
    print("GRADE A")
elif marks <= 90 and marks >= 81:
    print("GRADE B")
elif marks <= 80 and marks >= 71:
    print("GRADE C")
elif marks <= 70 and marks >= 1:
    print("FAIL")
else:
    print("Invalid Number")
