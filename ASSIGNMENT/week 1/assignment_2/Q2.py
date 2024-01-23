"""
Q2. A student will not be allowed to sit in exam if his/her attendance is less than 75%. 
Take following input from user

1.Number of classes held
2.Number of classes attended.

1. Print percentage of class attended
2. Print Is student is allowed to sit in exam or not
"""

classes_held: int = int(input("Enter The Classes Held = "))
classes_attended: int = int(input("Enter The Classes attended = "))

percentage = classes_attended * 100 / classes_held

print(
    f"Total Classes Held = {classes_held}\nTotal Classes Attended = {classes_attended}\nPercentage = {percentage:.2f}%"
)

if percentage >= 75:
    print(f"sit in exam")
else:
    print("Not Sit")



