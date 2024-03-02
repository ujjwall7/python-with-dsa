a = {
    "physics": 19,
    "chemistry": 79,
    "english": 49,
    "maths": 39,
}

print(a)
print(a.items()) #changed in tuple
sorted_x = sorted(a.items(), key = lambda x:x[1])

print(sorted_x)



