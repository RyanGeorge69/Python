lim=int(input("Enter the limit="))
sum=1
for i in range(1,lim+1):
    print("1/",i,end=" +")
    sum=sum+(1/i)
print("\n=",sum)