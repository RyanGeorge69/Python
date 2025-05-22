list1= [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]
print(list1)

for x in list1:
    if list1.count(x)>1:
        list1.remove(x)

print(list1)