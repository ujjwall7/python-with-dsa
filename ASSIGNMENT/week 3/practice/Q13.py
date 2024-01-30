"""
                  * 
                * * *
              * * * * *
            * * * * * * *
          * * * * * * * * *
        * * * * * * * * * * *
          * * * * * * * * *
            * * * * * * *
              * * * * *
                * * *
                  *
"""

def trianglePattern(n: int = 0):
    for i in range(1, n + 1):
        for j in range(1, n - i + 1):
            print(" ", end=' ')

        for k in range(1, 2 * i):
            print("*", end=' ')
        print()

    for i in range(n-1, 0, -1):  # for i number of lines
        for j in range(n-1, i-1, -1):
            print(" ", end=' ')
        for k in range(2 * i -1):
            print("*", end= " ")
        print()

        


trianglePattern(5)








