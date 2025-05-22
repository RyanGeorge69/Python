marks = {
    "ram": 33,
    "rahul": 15,
    "devesh": 30,
    "jayul": 34,
    "jiya": 16,
    "sadhana": 11,
    "meena": 19,
    "karan": 20
}

print("Name\tMarks\tResult")
for k,v in marks.items():
    if v>=18:
        print(k,"\t",v,"\tpass")
    else:
        print(k,"\t",v,"\tfail")