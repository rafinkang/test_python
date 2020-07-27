# 파이썬 객체를 파일에 저장하는 과정을 Pickling 이라고 한다.
# 파이썬 객체를 읽어오는 과정을 Unpickling 이라고 한다.

import pickle

name = "쑤진공주"
age = 20
addrs = "율도국"
strength = 7
intelligence = 3
money = 0
exp = 10
level = 3

# 바이너리타입 - 쓰기 모드로 열기
with open('./day9/LOL.dat', 'wb') as file:
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(addrs, file)
    pickle.dump(strength, file)
    pickle.dump(intelligence, file)
    pickle.dump(money, file)
    pickle.dump(exp, file)
    pickle.dump(level, file)