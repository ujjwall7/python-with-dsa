"""
Q5. .Write a program to calculate bill 
Ask the final amount from the user.
You have to give discount and print the final bill after discount.
50000 above - 30% 
discount 40000 - 49999 - 25% 
discount 30000 - 39999 - 20% 
discount 10000 - 29999 - 10% 
discount 1 - 9999 - No discountPrint the discount and the final amount to be paid.

Example 1
Enter bill amount = 80000 
You got 30% discountYour final bill is Rs. 56000
"""

def calculate_bill_amount(num):
    discount = 1
    if num >= 50000:
        discount = 30 / 100
    elif num >= 40000 and num <= 49999:
        discount = 25 / 100
    elif num >= 30000 and num <= 39999:
        discount = 20 / 100
    elif num >= 10000 and num <= 29999:
        discount = 10 / 100
    elif num >= 1 and num <= 9999:
        discount = 1
    else:
        print("Inavlid")

    if not discount == 1:
        discount_amount = num * discount
        final_amount = num - discount_amount
        print(f"Your Finalize prize is {final_amount} Rs")
    else:
        print(f"Your Finalize prize is {num} Rs")

calculate_bill_amount(10000)

