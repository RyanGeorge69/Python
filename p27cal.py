print("Press 1 for addtion")
print("Press 2 for subtraction")
print("Press 3 for multiplication")
print("Press 4 for divition")
op=int(input("Enter option=>"))

if op==1:
    no1=int(input("Enter 1st no.=>"))
    no2=int(input("Enter 2nd no.=>"))
    print("Addtion =",no1+no2)
elif op==2:
    no1 = int(input("Enter 1st no.=>"))
    no2 = int(input("Enter 2nd no.=>"))
    print("Subtraction =", no1-no2)
elif op==3:
    no1 = int(input("Enter 1st no.=>"))
    no2 = int(input("Enter 2nd no.=>"))
    print("multiplication =", no1*no2)
elif op==4:
    no1 = int(input("Enter 1st no.=>"))
    no2 = int(input("Enter 2nd no.=>"))
    print("division =", no1/no2)
else:
    print("Wrong input")