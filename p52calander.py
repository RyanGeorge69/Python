mon=int(input("Enter the month number="))
yer=int(input("Enter the year ="))

if mon==1:
    print("january ",yer," has 31 days")
elif mon==2 and yer%4==0:
    print("February ", yer, " has 29 days")
elif mon==2:
    print("February ", yer, " has 28 days")
elif mon==3:
    print("march ", yer, " has 31 days")
elif mon==4:
    print("April ", yer, " has 30 days")
elif mon==5:
    print("may ", yer, " has 31 days")
elif mon==6:
    print("june ", yer, " has 30 days")
elif mon==7:
    print("july ", yer, " has 31 days")
elif mon==8:
    print("august ", yer, " has 31 days")
elif mon==9:
    print("September ", yer, " has 30 days")
elif mon==10:
    print("October ", yer, " has 31 days")
elif mon==11:
    print("november ", yer, " has 30 days")
elif mon==12:
    print("Decamber ", yer, " has 31 days")