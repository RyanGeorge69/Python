f1=open("abc", "r")
rev=[]
while True:
    ch=f1.read(1)

    if not ch:
        break
    rev.append(ch)

f1.close()
rev.reverse()
for x in rev:
    print(x,end="")

"""

"""