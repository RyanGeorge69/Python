no=int(input("Enter the number of rows:"))
for i in range(1,no+1):
    for j in range(1,no+1):
        if i == 1 or i == no or j == 1 or j == no:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("")