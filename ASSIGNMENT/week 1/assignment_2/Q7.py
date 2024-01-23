"""
Q7. Take Salary as input from User and Update the salary of an employee.
salary less than 10,000, 5 % increment
salary between 10,000 and 20, 000, 10 % increment
salary between 20,000 and 50,000, 15 % increment
salary more than 50,000, 20 % increment
"""

salary: int = int(input("Enter the number = "))
updated_salary = 0
if salary <= 10000:
    percent = salary * 5 / 100
    updated_salary = salary + percent

elif salary > 10000 and salary <= 20000:
    percent = salary * 10 / 100
    updated_salary = salary + percent

elif salary > 20000 and salary <= 50000:
    percent = salary * 15 / 100
    updated_salary = salary + percent

elif salary > 50000:
    percent = salary * 20 / 100
    updated_salary = salary + percent

else:
    print("Invalid Number")

print(updated_salary)
