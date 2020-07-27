import time

# help(모듈) : 모듈에대한 설명
# help(time)
# help(time.time)

# print(time.time())
print(time.ctime(), type(time.ctime()))
t = time.ctime().split()
print(t, t[4])

# 지금 시간을 1초에 한번씩 출력하고싶다.
# for i in range(100):
# while True:
#     print(time.ctime())
#     time.sleep(1)

print(dir(time))