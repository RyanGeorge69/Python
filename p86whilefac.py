no = int(input("Enter limit =>"))
i = no
pro=1
while i >= 1:
    print(i,end="*")
    pro*=i
    i -=1
print("\n=",pro)