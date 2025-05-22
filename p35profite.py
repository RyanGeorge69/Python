buy=int(input("Enter the buying price="))
sell=int(input("Enter the selling price="))

pro=sell-buy

if pro>0:
    print("The user has a profit")
elif pro<0:
    print("The user has a loss")
else:
    print("The user has no profit or loss")