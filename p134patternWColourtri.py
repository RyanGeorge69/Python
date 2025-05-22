from colorama import Fore
no=int(input("Enter the number of rows="))

for i in range(0,no):
    for j in range(0,i):
        print(" ", end="")
    for j in range(0,no - i):
        print(Fore.RED, end="")
        print("* ", end="")
    for j in range(0,i * 2):
        print(" ", end="")
    for j in range(0,no - i):
        print(Fore.YELLOW, end="")
        print("* ", end="")
    for j in range(0,i*2):
        print(" ",end="")
    for j in range(0,no - i):
        print(Fore.GREEN, end="")
        print("* ", end="")
    print()