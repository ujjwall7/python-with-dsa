"""
Q3. Make your own list. 
Write a Python program that takes an integer as an input, 
and make a new list containing the last n elements of the original list. Using slicing logic.

my_list = [10, -5, 8, 3, -1, -9, 7, 2]
n = 3
result = [9,7,2]
"""

my_list = [10, -5, 8, 3, -1, -9, 7, 2]
get_pos = int(input("Enter the Position = "))
print(my_list[-(get_pos)::1])

