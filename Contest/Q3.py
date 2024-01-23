"""
Q3. Make a function named printWords which accepts an integer n from
the user. Print the number as words.
"""

def printWords(num:int):
    num = str(num)
    for i in num:
        if i == str(0):
            print('Zero', end=' ')
        elif i == str(1):
            print('One', end=' ')
        elif i == str(2):
            print('Two', end=' ')
        elif i == str(3):
            print('Three', end=' ')
        elif i == str(4):
            print('Four', end=' ')
        elif i == str(5):
            print('Five', end=' ')
        elif i == str(6):
            print('Six', end=' ')
        elif i == str(7):
            print('Seven', end=' ')
        elif i == str(8):
            print('Eight', end=' ')
        elif i == str(9):
            print('Nine', end=' ')

printWords(1221)







