"""
Control Statements 
1. break
2. continue
"""


i = 1
while i < 10:
    print(i)
    i += 1
    if i == 5:
        break
    # print('ok')
    # print('done')
print('-------------------------')
i = 1
while i <= 10:
    i+=1
    if i==5:
        continue
    print(i)
