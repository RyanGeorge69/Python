f1=open("abc",'r')
upp=0
low=0
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch.isupper():
        upp+=1
    elif ch.islower():
        low+=1
print("No of consonant in uppercase ",upp)
print("No of consonant in lowercase ",low)
f1.close()