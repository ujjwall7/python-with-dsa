"""
Q2. Create a function sumCountOddEven that accepts an List of Integers and calculate sum of even and odd numbers.
"""


from typing import List



def sumCountOddEven(lst:List[int])->tuple:
    even_sum_count = 0
    odd_sum_count = 0

    for i in range(len(lst)):
        if lst[i]%2==0:
            even_sum_count+=lst[i]
        else:
            odd_sum_count+=lst[i]
    get_even_sum = f"Even Numbers Sum {even_sum_count}"
    get_odd_sum = f"Odd Numbers Sum {odd_sum_count}"
    return get_even_sum, get_odd_sum

my_list = [
    34,
    11,
    91,
    59,
    33,
    22,
]

print(sumCountOddEven(my_list))






