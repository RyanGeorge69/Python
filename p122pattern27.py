no=int(input("Enter the number of rows:"))
k=5
for i in range(1,no+1):
    for j in range(1,i):
        print(" ",end="")
    for j in range(no,i-1,-1):
        print(k,end="")
    k-=1
    print("")