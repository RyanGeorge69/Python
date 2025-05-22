no1=int(input("Enter the number of elements for the list : "))
List1=[]

for i in range(no1):
    List1.append(int(input("Enter the element: ")))

even=0
odd=0
for i in List1:
    if i%2==0:
        even+=1
    else:
        odd+=1

print("Even count is: ",even)
print("Odd count is: ",odd)