temp=int(input("Enter the temperature="))

if temp<=0:
    print("Freezing Atmosphere")
elif temp>0 and temp<=10:
    print("Very cold atmosphere")
elif temp>10 and temp<=20:
    print("Cold Atmosphere")
elif temp>20 and  temp<=30:
    print("Normal Atmospher")
elif temp>30 and temp<=40:
    print("Hot Atmospher")
else:
    print("Very hot Atmospher")