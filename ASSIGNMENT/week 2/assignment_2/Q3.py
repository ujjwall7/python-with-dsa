"""
Q3. Ask 3 numbers from user. 
Make a function which returns the middle of those 3 numbers. 
Then make a function to check if that middle number is divisible by both 3 and 4. 
Make 2 functions for reusability.
"""

def checkNumberDivisibleBy3And4(a:int):
  if a%3==0 and a%4==0:
    return "Number is Divisile by 3 and 4"
  else:
    return "Not Number is Divisile by 3 and 4"

def middleOfThree(
    a: int,
    b: int,
    c: int,
):
  result = checkNumberDivisibleBy3And4(b)  
  return result

print(middleOfThree(1,12,3))

