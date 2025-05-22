no1=int(input("Enter the number of elements for the list 1: "))
List1=[]

for i in range(no1):
    List1.append(int(input("Enter the element: ")))

print(List1.index(max(List1)))