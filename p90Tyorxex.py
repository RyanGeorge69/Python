#typing(50>20rep else 15rep) and xerox(50>3rep else 2)
total=0
while True:
    print("Enter 1 for typing")
    print("Enter 2 for xerox")
    print("Enter 3 to exit")
    op = int(input("Enter option=>"))

    if op==1:
        qun = int(input("Enter the quantity=>"))
        if qun>=50:
            print("Your total is ", qun *15)
            total+=(qun*15)
        else:
            print("Your total is ",qun*20)
            total += (qun * 20)
    if op==2:
        qun = int(input("Enter the quantity=>"))
        if qun >=50:
            print("Your total is ", qun*2)
            total += (qun *2)
        else:
            print("Your total is ", qun * 3)
            total += (qun*3)
    if op==3:
        print("Your total=",total)
        print("Bye")
        break