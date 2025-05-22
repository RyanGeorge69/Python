import time
current = time.localtime(time.time())
h=current.tm_hour
m=current.tm_min
if current.tm_hour < 12:
    print(h,":",m,"AM")
else:
    print(h-12,":",m,"PM")