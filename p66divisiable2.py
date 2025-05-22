n=int(input("Enter the limit="))
di=int(input("Enter the divider="))
for i in range(1,n+1):
    if i%di==0:
        print(i," is divisiable with ",di)
    else:
        print(i," is not divisiable with ",di)