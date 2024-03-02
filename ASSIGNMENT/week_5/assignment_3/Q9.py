"""
153 = 1^3 + 5^3 + 3^3
"""

starting_number = int(input("Enter the starting number = "))
ending_number = int(input("Enter the ending number = "))
for i in range(starting_number, ending_number + 1):
    armstrong = 0
    power_check = int(len(str(i))) # type: ignore
    convert_str = str(i)
    # print(f"{power_check = }")
    for j in convert_str:
        armstrong+=int(j)**power_check 
    if i == armstrong:
        print(f"{armstrong = }")




