no=int(input("Enter the number of elements in the list: "))
Sample_List=[]
for i in range(no):
    Sample_List.append(input("Enter the element: "))
y=int(input("Enter position="))
x=int(input("Enter Value="))
Sample_List.insert(y-1,x)
print(Sample_List)