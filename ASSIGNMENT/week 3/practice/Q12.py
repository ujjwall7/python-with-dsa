"""
                  * 
                * * *
              * * * * *
            * * * * * * *
          * * * * * * * * *
        * * * * * * * * * * *
"""

for i in range(1, 10+1):
    count = 1
    for j in range(1, 10-i+1):
        print(" ", end=" ")

    for k in range(1,2*i):
        print("*", end=" ")
        count+=2
    print()












