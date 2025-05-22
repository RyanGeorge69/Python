"""
The set that has all the elements of another set is called a superset
"""
set1={11,22,33,44,55,66}
set2={11,33,55}
set3={1,2,3,4,9,11,55,66}
set4={8,9,7}

print(set1.issuperset(set2))
print(set1.issuperset(set3))
print(set1.issuperset(set4))
