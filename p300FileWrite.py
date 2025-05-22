f1=open("abc", "r")
f2=open("abc1","w")
while True:
    ch=f1.read(1)
    if not ch:
        break
    f2.write(ch)
f1.close()
f2.close()
print("done")