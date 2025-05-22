no=int(input("Enter the number of rows:"))
for i in range(1,no+1):
    K = 5
    for j in range(no,i-1,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print(K,end="")
        K-=1
    print("")