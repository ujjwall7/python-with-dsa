"""
Q2. Make your own list of numbers. Ask a start and end position from User. 
Make another dierent list which will contain number from start to end position. 
Use slicing logic

my_list = [10, -5, 8, 3, -1, -9, 7, 2]

Enter Start Position = 2
Enter End Position = 5
Result = [8, 3, -1, -9]
"""

start_pos = int(input("Enter Start Position = "))
end_pos = int(input("Enter End Position = "))
my_list = [10, -5, 8, 3, -1, -9, 7, 2]

print(my_list[start_pos:end_pos+1])




