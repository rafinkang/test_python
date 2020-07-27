import pickle

# 바이너리타입 읽어오기 rb (read bytes)
with open('./day9/LOL.dat', 'rb') as file:
    name = pickle.load(file)
    age = pickle.load(file)
    addrs = pickle.load(file)
    strength = pickle.load(file)
    intelligence = pickle.load(file)
    money = pickle.load(file)
    exp = pickle.load(file)
    level = pickle.load(file)

print("이름 : ", name)
print("나이 : ", age)
print("주소 : ", addrs)
print("힘 : ", strength)
print("지능 : ", intelligence)
print("돈 : ", money)
print("경험치 : ", exp)
print("레벨 : ", level)