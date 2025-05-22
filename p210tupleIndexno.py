t1 = (11, 22, 33, 44, 55)
print(t1)
no=int(input("Enter an element =>"))
if no in t1:
    print(t1.index(no))
else:
    print("The number you entered is not in the tuple")