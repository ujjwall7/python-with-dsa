""""
Q1. Create a function that takes three numbers as parameters 
and returns the largest among them. 
Also if no arguments are passed, 
make sure the parameters take default value as None and return answer as -1.
"""


# Without Annotations
def largest(n1=None, n2=None, n3=None):
    if n1 != None and n2 != None and n3 != None:
        if n1 > n2 and n1 > n3:
            return n1
        if n2 > n1 and n2 > n3:
            return n2
        else:
            return n3
    else:
        return -1


# With Annotations
# int | None --- It means it can be an int or None
def largestPart2(
    n1: int | None = None,
    n2: int | None = None,
    n3: int | None = None,
) -> int:
    if n1 != None and n2 != None and n3 != None:
        if n1 > n2 and n1 > n3:
            return n1
        if n2 > n1 and n2 > n3:
            return n2
        else:
            return n3
    else:
        return -1


print(largest(12, 3, 554))
print(largestPart2(12, 3, 554))

print(largest())
print(largestPart2())
