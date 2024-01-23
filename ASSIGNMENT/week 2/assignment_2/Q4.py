"""
Q4. Write a Python program that takes four numbers from the user. 
Implement a function to find the average of the first three numbers. 
Then, create another function to check if the average is greater than or equal to the fourth number. 
Make sure to use these two functions to determine and print whether the average 
is greater than or equal to the fourth number or not.
"""


def checkAverage(
    a: int,
    b: int,
    c: int,
    d: int,
):
    _sum = a + b + c
    average = _sum / 3

    if average <= d:
        comparision_result = f"Average is less than {d}"
    else:
        comparision_result = f"Average is greater than {d}"

    average_return = f"The Average of {a}, {b} and {c} is {average}"

    return comparision_result, average_return


result, avg = checkAverage(1, 2, 3, 4)
print(result)
print(avg)
