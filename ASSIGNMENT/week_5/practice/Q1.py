details = {
    "anirudh" : [12,43,54],
    "akul" : [12,65,86],
    "muskan" : [98,99,89]
}


highest = details["anirudh"][0]
key = ""
value = ""
for key, value in details.items():
    print(f"{key} = {sum(value)}")
    check = sum(value)
    if highest<check:
        highest = check
        key = key
        value = check

print(f"{key}={value}")
    




