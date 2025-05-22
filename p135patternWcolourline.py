from colorama import *
no=int(input("Enter the number of rows="))
tem=no
for i in range(0,no):
    if i==tem-no:
        print(Fore.MAGENTA, end="")
    if i==tem-no+1:
        print(Fore.RED, end="")
    if i==tem-no+2:
        print(Fore.CYAN, end="")
    if i == tem - no+3:
        print(Fore.BLUE, end="")
    if i == tem - no + 4:
        print(Fore.GREEN, end="")
    for j in range(0,i):
        print(" ", end="")
    for j in range(0,no - i):
        print("* ", end="")
    for j in range(0,i * 2):
        print(" ", end="")
    for j in range(0,no - i):
        print("* ", end="")
    for j in range(0,i*2):
        print(" ",end="")
    for j in range(0,no - i):
        print("* ", end="")
    print(Fore.RESET, end="")
    print()