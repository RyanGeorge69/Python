no=int(input("Enter a number="))

for i in range(no,0,-1):
    k=1
    for j in range(i,0,-1):
        if k%2==0:
            print("0 ",end="")
        else:
            print("1 ",end="")
        k+=1
    print("")