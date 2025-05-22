students={1:"Ram", 22:"Jayul", 3:"Rahul",44:"Anjali",50:"Riya"}
students.setdefault(101,"Sita")
print(students)

students.setdefault(102,"")
print(students)

students[102]="Ravan"
print(students)