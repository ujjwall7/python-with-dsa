"""
Q1. There are two variables.a=5 b=10 What will be the output of following:
a > 5 and b >= 10
a >= 5 or not b > 10
not ( a > 5 and b > 5)
not ( a < 10 or not b < 10)
not ( not a <= 5 or not b >= 10)
"""
a = 5
b = 10

print(a > 5 and b >= 10)  # output = False
print(a >= 5 or not b > 10)  # output = True
print(not (a > 5 and b > 5)) # output = True
print(not (a < 10 or not b < 10)) # output = False
print(not (not a <= 5 or not b >= 10)) # output = True
