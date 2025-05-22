import time
current = time.localtime(time.time())

if current.tm_hour < 12:
    print("Good morning")
elif 12<current.tm_hour < 18:
    print("Good afternoon")
else:
    print("Good evening")