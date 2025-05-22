lim=int(input("Enter the limit="))
sum=0
for i in range(1,lim+1):
    if lim%i==0:
        sum=sum+1
if sum>2:
    print("It is not a prime number")
else:
    print("It is a prime number")