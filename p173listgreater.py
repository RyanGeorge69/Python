no=int(input("Enter the number of elements in the list: "))
Samplist=[]
for i in range(no):
    Samplist.append(int(input("Enter the element: ")))

gre=int(input("Enter a number: "))

for i in Samplist:
    if i>gre:
        print(i)