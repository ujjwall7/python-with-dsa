"""
Palindrome
"""

def reverse(num:int):
    n:int = num
    reverse=0
    while n>0:
        reminder = n%10
        reverse = reverse * 10 +reminder
        n=n//10
    return reverse

def Palindrome(n:int):
    reverse_num = reverse(n)
    if n==reverse_num:
        print("Palindrome")
    else:
        print("Not Palindrome")

Palindrome(222)






