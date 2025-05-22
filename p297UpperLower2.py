f1=open("abc",'r')
u=0
l=0
o=0
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch.isupper():
        u=u+1
    elif ch.islower():
        l=l+1
    else:
        o=o+1
f1.close()
print("Upper case letters:",u)
print("Lower case letters:",l)
print("Other characters:",o)