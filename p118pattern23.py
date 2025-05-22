no = int(input("Enter a number="))
k = 1
for i in range(no, 0, -1):

    for j in range(i, 0, -1):
        if i%2==0:
            print("0 ", end="")
        else:
            print("1 ",end="")

    print("")
