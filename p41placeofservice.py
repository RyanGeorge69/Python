age=int(input("Enter your age="))
gen=input("Enter M for male and F for female=")

if gen=='Y' :
    print("you can only work in the urban area")
elif gen=='M' and age>=20 or age<40:
    print("You may work anywhere")
elif gen=='M'  and age>=40 or age<60:
    print("You can only work in urban areas ")
else:
    print("Error")