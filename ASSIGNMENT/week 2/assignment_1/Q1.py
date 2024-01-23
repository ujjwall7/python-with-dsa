def minimum(a,b,c):
    smallest = a
    if b < smallest:
        smallest = b
    if c < smallest:
        smallest = c
    print(f"{smallest} = smallest number")

def maximum(a,b,c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    print(f"{largest} = largest number")

minimum(15,2,42)
maximum(15,2,402)








