no1=int(input("Enter the number of elements for the list 1: "))
List1=[]
list2=[]
for i in range(no1):
    List1.append(int(input("Enter the element: ")))

for x in List1:
    list2.append(x*x)

print(List1)
print(list2)