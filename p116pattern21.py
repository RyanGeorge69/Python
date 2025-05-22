no = int(input("Enter a number="))
k=1
for i in range(no, 0, -1):

    for j in range(i, 0, -1):
        print(k, end="")
    k+=1
    print("")
