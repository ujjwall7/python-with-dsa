"""
Q8. Take 10 integer inputs from user and store them in a list. 
Now, copy all the elements in another list but in reverse order.
"""


def reverseList(num: list[int]):
    left = 0
    right = len(num) - 1
    while left < right:
        temp = num[left]
        num[left] = num[right]
        num[right] = temp
        left += 1
        right -= 1
    return num


i = 1
new_list = []
while i <= 3:
    num = int(input("Enter the number = "))
    new_list.append(num)
    i += 1
print(new_list)
print(reverseList(new_list))


# for i in range(10, 0, -1):
#     print(i, end=' ')
# print()

# for i in range(10-1, -1, -1):
#     print(i, end=' ')
