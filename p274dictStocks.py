stocks={"info":[600,630,620],"ril":[1430,1490,1567],"mtl":[234,180,160]}
s=0
while True:
    print("Press 1 for stocks to print")
    print("Enter 2 to add Stock")
    print("Enter 3 to Exit")
    op=int(input("Enter option=>"))
    if op==1:
        print("Stock name\t\tstock price\t\taverage price")
        for k, v in stocks.items():
            m1, m2, m3 = v
            s = sum(v)
            print(k, "\t", stocks[k], "\t", s/3)
        print()
    elif op==2:
        name = input("Enter Stocks name=>").lower()
        if name not in stocks:
            a=int(input("Enter Stock price=>"))
            b=int(input("Enter Stock price=>"))
            c=int(input("Enter Stock price=>"))
            list1=[a,b,c]
            stocks[name] = list1
        else:
            print("Stock already present")
        print()

    elif op==3:
        print("Exiting")
        print("Stock\tprice")
        for i in stocks:
            print(i, "\t", stocks[i])
        break