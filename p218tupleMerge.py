t1 = (11, 22, 33)
t2 = (44, 55, 66)

list1=list(t1)
list2=list(t2)
list1.extend(list2)
t1=tuple(list1)
print(t1)