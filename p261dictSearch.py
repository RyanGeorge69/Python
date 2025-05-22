marks = {
    "ram": 33,
    "rahul": 45,
    "manav": 30,
    "jayul": 34,
    "meena": 29,
    "siddhi": 48
}

name=input("Enter the name of the student: ")
c=0
for k,v in marks.items():
    if k==name:
        print("Yes, it exists")
        c=1

if c==0:
    print("No, it doesn't exist")