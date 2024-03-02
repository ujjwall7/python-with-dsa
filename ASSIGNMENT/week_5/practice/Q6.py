a = [
    ("physics", 19),
    ("chemistry", 79),
    ("english", 49),
    ("maths", 39),
]


print(a[0], type(a[0]))
print(a[-1], type(a[-1]))

a.sort(key = lambda x : x[1])
# sort ek method hai,
# key se sort karta hai 
# lambda x : x[1] ek ek karke index number 1 par deta jayega or sor karega number ke base par
print(a)










