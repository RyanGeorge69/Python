f1=open("abc", "r")
f2=open("abc1","w")
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
        f2.write(ch)
f1.close()
f2.close()
print("done")

"""
1) 1-2 space X
2) 1-2 , vowel 7
3)1-2 vowel
3  other
4) 1-2 upper
3 lower
"""