"""
Q4. Make your own list. 
Write a Python program that takes an integer as an input, 
and make a new list containing the last n elements of the original list but in reverse order. 
Using slicing logic.

my_list = [10, -5, 8, 3, -1, -9, 7, 2]
n = 4
result = [2, 7, -9, -1]
"""

my_list = [10, -5, 8, 3, -1, -9, 7, 2]
get_pos = int(input("Enter the Position = "))
print(my_list[-1:-(get_pos)-1:-1])

