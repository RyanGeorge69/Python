print("Enter 1 for Max2")
print("Enter 2 for Max3")
op=int(input("Enter option=>"))

if op==1:
    no1=int(input("Enter the 1st no.=>"))
    no2=int(input("Enter the 2st no.=>"))
    if no1>no2:
        print(no1,"is greater")
    else :
        print(no2,"is greater")
elif op==2:
    no1=int(input("Enter the 1st no.=>"))
    no2=int(input("Enter the 2st no.=>"))
    no3=int(input("Enter the 3rd no.=>"))
    if no1>no2 and no1>no3:
        print("no1 is greater")
    elif no1<no2 and no2>no3:
        print("no2 is greater")
    elif no1>no2 and no1<no3:
        print("no3 is greater")
    else:
        print("All are equal")

else:
    print("Wrong input")

#7874391191