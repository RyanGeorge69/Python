from colorama import Fore,Style
list1=["-","-","-","-","-","-","-","-","-"]
turn=1
print("Tic Tac Toe")
while turn<10:
    print("Turn", turn)
    print(list1[0], list1[1], list1[2])
    print(list1[3], list1[4], list1[5])
    print(list1[6], list1[7], list1[8])


    if turn%2==0:
        po=int(input("Enter the position to place X="))
        if po > 9 or po < 1 or list1[po - 1] != "-":
            print("Invalid or already occupied position")
            turn -= 1
            continue
        else:
            list1[po-1]=f"{Fore.RED}X{Style.RESET_ALL}"
            turn = turn + 1
            print(list1[0], list1[1], list1[2])
            print(list1[3], list1[4], list1[5])
            print(list1[6], list1[7], list1[8])

    if turn % 2 != 0:
        po = int(input("Enter the position to place O="))
        if po > 9 or po < 1 or list1[po - 1] != "-":
            print("Invalid or already occupied position")
            turn -= 1
            continue

        else:
            list1[po - 1] = f"{Fore.BLUE}O{Style.RESET_ALL}"
            turn = turn + 1

    if list1[0] == f"{Fore.RED}X{Style.RESET_ALL}" and list1[1] == f"{Fore.RED}X{Style.RESET_ALL}" and list1[
        2] == f"{Fore.RED}X{Style.RESET_ALL}":
        print("\nX player wins")
        print(list1[0], list1[1], list1[2])
        print(list1[3], list1[4], list1[5])
        print(list1[6], list1[7], list1[8])
        turn = 15
        break
    elif list1[3] == f"{Fore.RED}X{Style.RESET_ALL}" and list1[4] == f"{Fore.RED}X{Style.RESET_ALL}" and list1[
        5] == f"{Fore.RED}X{Style.RESET_ALL}":
        print("\nX player wins")
        print(list1[0], list1[1], list1[2])
        print(list1[3], list1[4], list1[5])
        print(list1[6], list1[7], list1[8])
        turn = 15
        break
    elif list1[6] == f"{Fore.RED}X{Style.RESET_ALL}" and list1[7] == f"{Fore.RED}X{Style.RESET_ALL}" and list1[
        8] == f"{Fore.RED}X{Style.RESET_ALL}":
        print("\nX player wins")
        print(list1[0], list1[1], list1[2])
        print(list1[3], list1[4], list1[5])
        print(list1[6], list1[7], list1[8])
        turn = 15
        break
    elif list1[0] == f"{Fore.RED}X{Style.RESET_ALL}" and list1[3] == f"{Fore.RED}X{Style.RESET_ALL}" and list1[
        6] == f"{Fore.RED}X{Style.RESET_ALL}":
        print("\nX player wins")
        print(list1[0], list1[1], list1[2])
        print(list1[3], list1[4], list1[5])
        print(list1[6], list1[7], list1[8])
        turn=15
        break
    elif list1[1] == f"{Fore.RED}X{Style.RESET_ALL}" and list1[4] == f"{Fore.RED}X{Style.RESET_ALL}" and list1[
        7] == f"{Fore.RED}X{Style.RESET_ALL}":
        print("\nX player wins")
        print(list1[0], list1[1], list1[2])
        print(list1[3], list1[4], list1[5])
        print(list1[6], list1[7], list1[8])
        turn = 15
        break
    elif list1[2] == f"{Fore.RED}X{Style.RESET_ALL}" and list1[5] == f"{Fore.RED}X{Style.RESET_ALL}" and list1[
        8] == f"{Fore.RED}X{Style.RESET_ALL}":
        print("\nX player wins")
        print(list1[0], list1[1], list1[2])
        print(list1[3], list1[4], list1[5])
        print(list1[6], list1[7], list1[8])
        turn = 15
        break
    elif list1[0] == f"{Fore.RED}X{Style.RESET_ALL}" and list1[4] == f"{Fore.RED}X{Style.RESET_ALL}" and list1[
        8] == f"{Fore.RED}X{Style.RESET_ALL}":
        print("\nX Player wins")
        print(list1[0], list1[1], list1[2])
        print(list1[3], list1[4], list1[5])
        print(list1[6], list1[7], list1[8])
        turn = 15
        break
    elif list1[2] == f"{Fore.RED}X{Style.RESET_ALL}" and list1[4] == f"{Fore.RED}X{Style.RESET_ALL}" and list1[
        6] == f"{Fore.RED}X{Style.RESET_ALL}":
        print("\nX Player wins")
        print(list1[0], list1[1], list1[2])
        print(list1[3], list1[4], list1[5])
        print(list1[6], list1[7], list1[8])
        turn = 15
        break

    # Check if O wins
    if list1[0] == f"{Fore.BLUE}O{Style.RESET_ALL}" and list1[1] == f"{Fore.BLUE}O{Style.RESET_ALL}" and list1[
        2] == f"{Fore.BLUE}O{Style.RESET_ALL}":
        print("\nO player wins")
        print(list1[0], list1[1], list1[2])
        print(list1[3], list1[4], list1[5])
        print(list1[6], list1[7], list1[8])
        turn = 15
        break
    elif list1[3] == f"{Fore.BLUE}O{Style.RESET_ALL}" and list1[4] == f"{Fore.BLUE}O{Style.RESET_ALL}" and list1[
        5] == f"{Fore.BLUE}O{Style.RESET_ALL}":
        print("\nO player wins")
        print(list1[0], list1[1], list1[2])
        print(list1[3], list1[4], list1[5])
        print(list1[6], list1[7], list1[8])
        turn = 15
        break
    elif list1[6] == f"{Fore.BLUE}O{Style.RESET_ALL}" and list1[7] == f"{Fore.BLUE}O{Style.RESET_ALL}" and list1[
        8] == f"{Fore.BLUE}O{Style.RESET_ALL}":
        print("\nO player wins")
        print(list1[0], list1[1], list1[2])
        print(list1[3], list1[4], list1[5])
        print(list1[6], list1[7], list1[8])
        turn = 15
        break
    elif list1[0] == f"{Fore.BLUE}O{Style.RESET_ALL}" and list1[3] == f"{Fore.BLUE}O{Style.RESET_ALL}" and list1[
        6] == f"{Fore.BLUE}O{Style.RESET_ALL}":
        print("\nO player wins")
        print(list1[0], list1[1], list1[2])
        print(list1[3], list1[4], list1[5])
        print(list1[6], list1[7], list1[8])
        turn = 15
        break
    elif list1[1] == f"{Fore.BLUE}O{Style.RESET_ALL}" and list1[4] == f"{Fore.BLUE}O{Style.RESET_ALL}" and list1[
        7] == f"{Fore.BLUE}O{Style.RESET_ALL}":
        print("\nO player wins")
        print(list1[0], list1[1], list1[2])
        print(list1[3], list1[4], list1[5])
        print(list1[6], list1[7], list1[8])
        turn = 15
        break
    elif list1[2] == f"{Fore.BLUE}O{Style.RESET_ALL}" and list1[5] == f"{Fore.BLUE}O{Style.RESET_ALL}" and list1[
        8] == f"{Fore.BLUE}O{Style.RESET_ALL}":
        print("\nO player wins")
        print(list1[0], list1[1], list1[2])
        print(list1[3], list1[4], list1[5])
        print(list1[6], list1[7], list1[8])
        turn = 15
        break
    elif list1[0] == f"{Fore.BLUE}O{Style.RESET_ALL}" and list1[4] == f"{Fore.BLUE}O{Style.RESET_ALL}" and list1[
        8] == f"{Fore.BLUE}O{Style.RESET_ALL}":
        print("\nO Player wins")
        print(list1[0], list1[1], list1[2])
        print(list1[3], list1[4], list1[5])
        print(list1[6], list1[7], list1[8])
        turn = 15
        break
    elif list1[2] == f"{Fore.BLUE}O{Style.RESET_ALL}" and list1[4] == f"{Fore.BLUE}O{Style.RESET_ALL}" and list1[
        6] == f"{Fore.BLUE}O{Style.RESET_ALL}":
        print("\nO Player wins")
        print(list1[0], list1[1], list1[2])
        print(list1[3], list1[4], list1[5])
        print(list1[6], list1[7], list1[8])
        turn=15
        break


if turn==10:
    print("It's tie")