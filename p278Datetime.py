import time
current=time.localtime(time.time())
h=current.tm_hour
m=current.tm_min
s=current.tm_sec
print(h,":",m,":",s)