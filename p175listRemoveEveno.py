no=int(input("Enter the number of elements in the list: "))
Samplist=[]
for i in range(no):
    Samplist.append(input("Enter the element: "))

for i in Samplist:
    if i%2==0:
        if i in Samplist:
            Samplist.remove(i)

print(Samplist)