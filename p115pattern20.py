no = int(input("Enter a number="))
for i in range(no, 0, -1):
    k=5
    for j in range(i, 0, -1):
        print(k, end="")
        k-=1
    print("")
