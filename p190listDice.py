import random
no=int(input("Enter number of dice to be rolled:"))
dice=[]
for i in range(no):
    y=random.randint(1, 6)
    dice.append(y)
a=0
for i in dice:
    if i==6:
        a+=1

print("The number of sixes are: ",a)