no1=int(input("Enter the number of elements for the list 1: "))
no2=int(input("Enter the number of elements for the list 2: "))
Sample_List1=[]
Sample_List2=[]
for i in range(no1):
    Sample_List1.append(input("Enter the element: "))
for i in range(no2):
    Sample_List2.append(input("Enter the element: "))

Sample_List1.extend(Sample_List2)
print(Sample_List1)
