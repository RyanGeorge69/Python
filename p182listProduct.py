no1=int(input("Enter the number of elements for the list 1: "))
List1=[]
pro=1
for i in range(no1):
    List1.append(int(input("Enter the element: ")))
    pro=pro*List1[i]

print(pro)