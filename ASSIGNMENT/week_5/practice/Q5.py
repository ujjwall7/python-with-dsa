students_details = {
    "anirudh" : {
        "age" : 12,
        "gender" : "Male",
        "address" : "sector 15 A Faridabad",
        "phone" : 100,
        "physics" : 23,
        "chemistry" : 81,
        "maths" :42
    },
    "akul" : {
        "age" : 19,
        "gender" : "Male",
        "address" : "sector 15 B Faridabad",
        "phone" : 101,
        "physics" : 23,
        "chemistry" : 81,
        "maths" :42
    },
    "megha" : {
        "age" : 23,
        "gender" : "FeMale",
        "address" : "sector 23 A Faridabad",
        "phone" : 912234502,
        "physics" : 23,
        "chemistry" : 81,
        "maths" :42
    },
}

#megha phone
# print(f"Megha phone = {students_details['megha']['address']}")

for keyss, val in students_details.items():
    total = val["physics"] + val["chemistry"] + val["maths"]
    val["total_marks"] = total
    print(val)

