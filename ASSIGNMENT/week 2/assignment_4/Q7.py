def pattern(nums: int):
    i = 1
    num = 0
    while i <= nums:
        print(num + 1, end=" ")
        if num == 0:
            num = 10
        else:
            num = num * 10
        i += 1


pattern(7)
