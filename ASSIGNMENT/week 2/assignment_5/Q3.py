def pattern(x: int, n: int):
    print(f"{x=}, {n=}")
    count = 1
    i=1
    calculation = 0
    while count <= n:
        if count == n:
            calculation += x/i
            print(f"{x}/{i} = {calculation}", end="")
            break
        calculation += x/i
        print(f"{x}/{i} + ", end = "")
        
        count+=1
        i+=2


x_var = int(input("Enter the x number = "))
n_var = int(input("Enter the n number = "))
pattern(n=n_var,x=x_var)

















