no=int(input("Enter a number="))

for i in range(1,no+1):
    k=5
    for j in range(1,i+1):
        print(k,end=" ")
        k-=1
    print("")
