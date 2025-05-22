from itertools import count

list1=[11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]
list2=[]
for x in list1:
    if list1.count(x)==1:
        list2.append(x)

list1=list2
print(list1)
