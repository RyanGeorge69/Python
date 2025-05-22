total=0
while True:
    print("Enter 1 for pizza(200rep)")
    print("Enter 2 for burger(250rep)")
    print("Enter 3 for fries(150rep)")
    print("Enter 4 for milkshake(100rep)")
    print("Enter 5 to exit")
    op=int(input("Enter option=>"))
    if op==1:
        qun=int(input("Enter the quantity=>"))
        print("Your total is ",qun*200," for ",qun," pizza")
        total+=(qun*200)
    elif op==2:
        qun=int(input("Enter the quantity=>"))
        print("Your total is ",qun*250," for ",qun," burger")
        total += (qun * 250)
    elif op==3:
        qun=int(input("Enter the quantity=>"))
        print("Your total is ",qun*150," for ",qun," fries")
        total += (qun * 150)
    elif op==4:
        qun=int(input("Enter the quantity=>"))
        print("Your total is ",qun*100," for ",qun," milkshake")
        total += (qun * 100)
    elif op==5:
        print("Total=",total)
        print("Bye")
        break
    else:
        print("Wrong input")