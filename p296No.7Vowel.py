f1=open("abc",'r')
vol=0
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch=="a"or ch=="e"or ch=="i"or ch=="o"or ch=="u"or ch=="A"or ch=="E"or ch=="I"or ch=="O"or ch=="U":
        print("7",end="")
        pass
    else:
        print(ch,end="")
f1.close()