"""
Q1. Make a dictionary with keys as subject name (physics, chemistry, etc.)
and values as their marks. Print the highest marks scored.
"""

def highestMarks(marks:dict)->int:
    highest_marks = marks['physics']
    # print(f"{highestMarks = }")

    for key, val in marks.items():
        if highest_marks < val:
            highest_marks = val
    return highest_marks


_new_dict = {
    'physics':12,
    'chemistry':605,
    'maths':99
}

obj = highestMarks(_new_dict)
print(obj)



