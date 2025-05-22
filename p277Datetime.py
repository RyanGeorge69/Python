import time
current = time.localtime(time.time())
y=current.tm_year
m=current.tm_mon
d=current.tm_mday
print(y,"/",m,"/",d)
