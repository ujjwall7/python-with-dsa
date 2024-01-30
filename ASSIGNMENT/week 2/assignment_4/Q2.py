"""
Q2. Create a function named pattern which takes an integer as an input
and print the following pattern.
"""


def pattern(num: int):
    i = 1
    while i <= num:
        print(i * 10)
        i+=1

pattern(4)
print()
print('-----')
pattern(11)