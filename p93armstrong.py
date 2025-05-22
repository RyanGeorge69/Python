no=int(input("Enter a number="))
no1=no
t=0
while no>0:
    rem=no%10
    t=t+rem*rem*rem #krishnamurthy
    no=no//10
if (t==no1):
    print("It is a armstrong no.")
else:
    print("It is not a armstrong no.")
