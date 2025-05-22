marks = {
    "ram": 33,
    "rahul": 15,
    "devesh": 30,
    "jayul": 34,
    "jiya": 16,
    "sadhana": 11,
    "meena": 19,
    "karan": 20,
    "anita": 25
}

a=0

for k,v in marks.items():
    if v>=18:
        a+=1

print("Number of students who passed the test=",a)