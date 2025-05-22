f1=open("abc",'r')
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch==" ":
        pass
    else:
        print(ch,end="")
f1.close()

"""
1)vowel ?
2) upper? lower?
3)vowel X
4) upper X
5) vowel 7
6) 1letter up 1leter lower
7) upper-lower , lower-upper
8) reverse
"""