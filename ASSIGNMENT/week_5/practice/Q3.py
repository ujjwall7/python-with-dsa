#map

# def convert(num):
#     return "shri narayan"

def convert(num):
    if num%2==0:
        return num
    else:
        pass

my_list = [22,32,43,24,243,134]
x = list(map(convert, my_list))
print(x)