lim=int(input("Enter the limit="))
pro=1
for i in range(lim,0,-1):
    print(i,"*",end="")
    pro=pro*i
print("\n=",pro)