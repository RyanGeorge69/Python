lim=int(input("Enter the limit="))
sum=1
for i in range(1,lim+1):
    print(i,end="*")
    sum=sum*i
print("\n=",sum)