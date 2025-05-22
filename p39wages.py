age=int(input("Enter age =>"))
gender=input("Enter gender =>")

if age>=18 and age<=30:
    if gender=="M":
        print("700")
    else:
        print("750")
elif age>30 and age<=40:
    if gender=="M":
        print("800")
    else:
        print("850")