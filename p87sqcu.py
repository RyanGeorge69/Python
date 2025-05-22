from colorama import Fore

while True:
    print(Fore.RED,"Press 1 for Square")
    print(Fore.RED,"Press 2 for Cube")
    print(Fore.RED, "Press 3 for Exit")
    a=int(input("Enter option: "))
    if a==1:
        no = int(input("Enter a number="))
        print(Fore.BLUE,"Square = ",no*no)
    elif a==2:
        no = int(input("Enter a number="))
        print("Cube = ",no*no*no)
    elif a==3:
        print("Bye")
        break
    else:
        print("Wrong input")