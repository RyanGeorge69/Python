def max(a, b):
    if a > b:
        return a
    elif b>a:
        return b
    else:
        return "Doth are same"


a=int(input("Enter a no="))
b=int(input("Enter a no="))
result = max(b=b, a=a)
print(result)
