"""
all the elements of set2 are present in set1 but set1 can have more elements is a subset,
not even 1 element can be different
"""
set1={11,22,33,44,55,66}
set2={11,33,55}
set3={1,2,3,4,9,11,55,66}
set4={8,9,7}

print(set2.issubset(set1))
print(set3.issubset(set1))
print(set4.issubset(set1))
