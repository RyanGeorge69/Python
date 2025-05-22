no=int(input("Enter the number of elements in the list: "))
Samplist=[]
for i in range(no):
    Samplist.append(int(input("Enter the element: ")))

Samplist2=Samplist.copy()
print(Samplist2)