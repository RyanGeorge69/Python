age=int(input("Enter you age="))

if age>=0 and age<=12:
    print("You are a child")
elif age>=13 and age<=19:
    print("You are a teenager")
elif age>=20 and age<65:
    print("You are an adult")
elif age>=65:
    print("you are a senior")
else:
    print("Wrong input")