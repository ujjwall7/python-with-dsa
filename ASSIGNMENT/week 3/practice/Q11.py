"""
        5 
      4 5
    3 4 5
  2 3 4 5
1 2 3 4 5
"""


for i in range(1, 5+1):
    for j in range(1, 5+1-i):
        print(" ", end=" ")
    for k in range(6-i,6):
        print(k, end=" ")
    print()















