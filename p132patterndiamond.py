from colorama import Fore
no=int(input("Enter the number of rows:"))
for i in range(1,no+1):
    print(Fore.BLUE, end="")
    for j in range(no,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("* ",end="")
    print("")
for i in range(1,no+1):
    print(Fore.BLUE, end="")
    for j in range(1, i+1):
        print(" ", end="")
    for j in range(no-1, i - 1, -1):
        print("* ", end="")
    print("")
