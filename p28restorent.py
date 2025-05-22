print("Enter 1 for pizza(200rep)")
print("Enter 2 for berger(250rep)")
print("Enter 3 for frise(150rep)")
print("Enter 4 for milkshake(100rep)")
op=int(input("Enter option=>"))

if op==1:
    qun=int(input("Enter the quantity=>"))
    print("Your total is ",qun*200," for ",qun," pizza")
elif op==2:
    qun=int(input("Enter the quantity=>"))
    print("Your total is ",qun*250," for ",qun," berger")
elif op==3:
    qun=int(input("Enter the quantity=>"))
    print("Your total is ",qun*150," for ",qun," frise")
elif op==4:
    qun=int(input("Enter the quantity=>"))
    print("Your total is ",qun*100," for ",qun," milkshake")
else:
    print("Wrong input")