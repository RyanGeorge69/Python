no = int(input("Enter limit =>"))
i = 1
pro=1
while i <= no:
    print(i,end="*")
    pro*=i
    i +=1
print("\n=",pro)