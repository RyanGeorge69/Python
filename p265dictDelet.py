marks = {
    "ram": 33,
    "rahul": 15,
    "devesh": 30,
    "jayul": 34,
    "jiya": 16,
    "sadhana": 11,
    "meena": 19
}
print(marks)
name =input("Enter the name to delete=")
del marks[name]
print(marks)