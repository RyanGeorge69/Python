no=int(input("Enter a number="))
no1=no
t=0
while no>0:
    rem=no%10
    f=1
    i=1
    no = no // 10
    while i <= rem:
            f*= i
            i += 1
    t+= f
if t==no1:
    print("It is a krishnamurthy no.")
else:
    print("It is not a krishnamurthy no.")
