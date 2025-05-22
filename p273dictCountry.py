Country_Population={
        "china":143,
        "india":136,
        "usa":32,
        "uk":21}
while True:
    print("Enter 1 to print Country Population")
    print("Enter 2 to add Country")
    print("Enter 3 to delete Country")
    print("Enter 4 For questioning")
    print("Enter 5 to exit")
    op=int(input("Enter option=>"))
    if op==1:
        print("country\tpopulation")
        for i in Country_Population:
            print(i, "\t", Country_Population[i])
        print()
    elif op==2:
        name=input("Enter country name=>").lower()
        if name not in Country_Population:
            pop=int(input("Enter country population=>"))
            Country_Population[name]=pop
        else:
            print("Country already present")
        print()
    elif op==3:
        name=input("Enter country name=>").lower()
        if name in Country_Population:
            del Country_Population[name]
        print()
        print()
    elif op==4:
        name = input("Enter country name=>").lower()
        print("The population is =",Country_Population.get(name))
        print()
    elif op==5:
        print("Exiting")
        print("country\tpopulation")
        for i in Country_Population:
            print(i,"\t",Country_Population[i])
        break