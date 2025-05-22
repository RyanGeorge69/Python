no1=int(input("Enter the number of elements for the list 1: "))
List1=[]

for i in range(no1):
    List1.append(input("Enter the element: "))

if List1[0]==List1[-1]:
    print("Both first and last number is same")
else:
    print("The last and first number is not same")
