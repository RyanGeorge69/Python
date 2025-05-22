t1 = (1, 2, 3, 4)
print(t1)
list1=list(t1)
list2=[]

for x in list1:
    list2.append(x*2)

t1=tuple(list2)
print(t1)