students_details = {
    "anirudh" : {
        "age" : 12,
        "gender" : "Male",
        "address" : "sector 15 A Faridabad",
        "phone" : 100
    },
    "akul" : {
        "age" : 19,
        "gender" : "Male",
        "address" : "sector 15 B Faridabad",
        "phone" : 101
    },
    "megha" : {
        "age" : 23,
        "gender" : "FeMale",
        "address" : "sector 23 A Faridabad",
        "phone" : 912234502
    },
}

#megha phone
# print(f"Megha phone = {students_details['megha']['address']}")

for keyss, val in students_details.items():
    # print(f"{key} = {val}")
    print(f"NAME = {keyss}")
    for key,val in val.items():
        print(f"{key} = {val}")
    print()

