"""
Q6. Write a Python code 
to split a list into two halves using list slicing. 
(Keep the length of list even).
"""

my_list = ["Anirudh", 6, 4, 110.654, True, -54]
mid: int = len(my_list) // 2
first_half = my_list[:mid]
second_half = my_list[mid:]
print(f"{first_half = }")
print(f"{second_half = }")