s1 = {11, 22, 33}
s2 = {44, 55, 66}
if not s1.isdisjoint(s2):
    print("The sets have common elements.")
else:
    print("The sets have no common elements.")
