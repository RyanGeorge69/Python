f1=open("abc",'r')
upp=0
low=0
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch.isupper():
        pass
    else:
        print(ch,end="")
f1.close()