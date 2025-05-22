import webbrowser

print("press 1 to open Google")
print("press 2 to open twitter")
print("press 3 to open youtube")
n=int(input())
if  n==1:
    webbrowser.open("https://www.google.com")
elif n==2:
    webbrowser.open("https://www.x.com")
elif n==3:
    webbrowser.open("https://www.youtube.com")
else:
    print("invalid input")