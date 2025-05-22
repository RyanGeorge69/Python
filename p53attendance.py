classheld=int(input("Enter the Number of class held="))
classattended=int(input("Enter the Number of class attended="))
a=classattended/classheld
if a*100>=75:
        print("You are allowed to give the test")
else:
    print("You are not allowed to give the test")