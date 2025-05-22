sl=int(input("Enter your suger level="))

if sl<80:
    print("Your suger level is low")
elif sl>=80 and sl<=100:
    print("Your suger level is normal")
elif sl>100:
    print("Your suger level is high")