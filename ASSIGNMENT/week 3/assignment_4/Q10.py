"""
Q10. Ask 10 numbers from the user and put them into the list. Now remove all the even numbers from that list.
"""

def removeAllEvenElements(lst:list[int]):
    new_odd_list = []
    for i in range(len(lst)):
        if lst[i]%2==0:
            pass
        else:
            new_odd_list.append(lst[i])

    return new_odd_list

i=1
my_list = []
while i<=10:
    num = int(input("Enter the number = "))
    print(num, end=' ')
    my_list.append(num)
    i+=1

print(removeAllEvenElements(my_list))







