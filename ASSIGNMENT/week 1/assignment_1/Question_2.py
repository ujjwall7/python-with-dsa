"""
Q2. Python program to convert kilometers to miles. Ask kilometer from User.
"""

kilometers: int = int(input("Enter the kilometers to convert into miles : "))
convert_into_miles = 0.62137 * kilometers
print(f"kilometers : {kilometers}\nconvert_into_miles : {convert_into_miles:.2f}")
