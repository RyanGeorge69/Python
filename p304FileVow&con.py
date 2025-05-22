f1=open("abc", "r")
f2=open("onlyVowel","w")
f3=open("onlyConsonant","w")
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
        f2.write(ch)
    else:
        f3.write(ch)
f1.close()
f2.close()
print("done")
