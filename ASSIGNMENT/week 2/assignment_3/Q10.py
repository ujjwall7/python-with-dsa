
def cal():
    count = 0
    numb = 0
    while True:
        number = int(input("Enter the nmber = "))
        count+=1
        numb+=number
        if number==0:
            average = numb/count
            return average
            break
print(cal())
