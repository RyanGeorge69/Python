no=int(input("Enter a number="))
for i in range(1,no+1):
    for j in range(1,no+1):
        if j%2==0:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print("")