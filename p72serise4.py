lim=int(input("Enter the limit="))
sum=0
for i in range(1,lim+1):
        print(i*i,end="+")
        sum=sum+(i*i)
print("\n=",sum)