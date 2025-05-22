lim=int(input("Enter the limit="))
sum=0
for i in range(1,lim+1):
    if i%2==0:
        print(i*i,end="+")
        sum=sum+(i*i)
    else:
        print(i*i*i, end="+")
        sum = sum + (i*i*i)
print("\n=",sum)