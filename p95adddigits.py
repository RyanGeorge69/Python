no=int(input("Enter a number="))
t=0
while no>0:
    rem=no%10
    t=t+rem
    no=no//10

print("total of the digits= ",t)
