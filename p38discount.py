pri=int(input("Enter the Marked price="))

if pri<=7000:
    print("your discount is 10% and net price is",pri-(pri*0.1))
elif pri>7000 and pri<=10000:
    print("your discount is 15% and net price is",pri-(pri*0.15))
elif pri>10000:
    print("your discount is 20% and net price is", pri - (pri*0.2))