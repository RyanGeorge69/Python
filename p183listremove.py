no1=int(input("Enter the number of elements for the list 1: "))
List1=[]

for i in range(no1):
    List1.append(input("Enter the element: "))

for i in range(no1):
    if len(List1[i])==0:
        print("The",i+1, "list is empty")
#
# else:
