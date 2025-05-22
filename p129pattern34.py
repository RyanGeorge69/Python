no=int(input("Enter the number of rows:"))
for i in range(1,no+1):
    for j in range(no,i-1,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("* ",end="")
    print("")
for i in range(1,no+1):
    for j in range(1,no+1):
        print(" * ",end="")
    print("")