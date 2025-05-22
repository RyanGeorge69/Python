import time
current = time.localtime(time.time())

if current.tm_year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")