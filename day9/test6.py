import time

print(time.time())
print(time.ctime())

print(type(time.gmtime()))
print(time.gmtime().tm_mon)
print(time.gmtime().tm_mday)