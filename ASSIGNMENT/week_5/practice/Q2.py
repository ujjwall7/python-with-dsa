def students(no:int):
    dic = {}
    for i in range(no):
        name = input("Enter the name = ")
        eng = int(input("Enter the marks 1 = "))
        mat = int(input("Enter the marks 2 = "))
        sci = int(input("Enter the marks 3 = "))
        dic[name] = [eng, mat, sci]
        print()
    return dic

number_of_students = int(input("Enter number of students = "))
print(students(number_of_students))

