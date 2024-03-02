"""
Q7. Store name as a Key, and 5 marks in a List as a value in dictionary. 
Store details of at least 5 students. 
Print the total marks with percentage of each and every student.
"""

def calculatePercent(total:int):
    return total * 100/500

def calculateMarks(students:list[dict]):
    for i in students:
        # print(i)
        for key, val in i.items():
            # print(f"{key} = {val}")
            if key=='marks':
                values_sum = calculatePercent(sum(val))
                print(f"name = {i['name']}, marks = {val}, percentage = {values_sum:.2f}")


students = [
    {"name": "Anirudh", "marks": [12, 43, 1, 76, 23]},
    {"name": "Akul", "marks": [78, 82, 80, 43, 62]},
    {"name": "Nihar", "marks": [13, 72, 32, 89, 53]},
    {"name": "Anusha", "marks": [43, 12, 79, 82, 85]},
    {"name": "Muskan", "marks": [54, 87, 72, 86, 84]},
]
# print(calculateMarks(students))
calculateMarks(students)





