get_json = """[{
    "quantity": 5,
    "description": "Item 1",
    "price": 50.99,
    "unit_price": 10.20
  },{
    "quantity": 3,
    "description": "Item 2",
    "price": 30.50,
    "unit_price": 10.17
  },{
    "quantity": 2,
    "description": "Item 3",
    "price": 20.10,
    "unit_price": 10.05
  }
]
"""   # postman form data se string mai aata hai data
print(type(eval(get_json)))
for x in eval(get_json):
    print(x, end=' ')

print()
print()

print(type(str(get_json)))
for x in str(get_json):
    print(x, end=' ')

print()
print()

print(type(get_json))
for x in get_json:
    print(x, end=' ')





 