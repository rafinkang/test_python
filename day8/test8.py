def make2(fn):
    # def test2():
    #     return "곤니찌와" + fn()
    return lambda : "곤니찌와 " + fn()

def make1(fn):
    return lambda : "니하오 " + fn()

# def 이름없음():
#   return "니하오" + fn()

def hello():
    return "한라봉"

hi = make2(make1(hello))
# hi = 람다식(익명함수)
print(hi())

# [] list
# {} set, json = dictionary 

def hello2():
    return "소망이"

print(make1(hello2)())
print(make2(hello2)())
print(make2(make1(hello2))())
print('--------------------------')
# 데코레이터 (decorator) : annotation - 장식하다, 꾸미다 라는 의미
# 장식하는 도구 
@make1
@make2
def hello2():
    return "소망이"
hi = hello2
print(hi())