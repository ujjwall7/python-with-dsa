"""
Q3. Create a function named pattern which takes an integer as an input
and print the following pattern.
"""

def pattern(num:int):
    i=1
    number = 1
    while i<=num:
        number *=2
        print(number, end=' ')
        i+=1

pattern(10)




