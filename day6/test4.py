def show_info(name, job, age, addr, height):
    # print("이름 :", name,"직업 :", job,"나이 :", age,"사는곳 :", addr,"키 :", height)
    print("이름 : {0}, 직업 : {1}, 나이 : {2}, 사는곳 : {3}, 키 : {4}".format(name, job, age, addr, height))

p = {'name':'홍길동', 'job':'도적', 'age':20, 'addr':'율도국', 'height':180.3}
print(p)

# **p -> 값이라고 추정되는 애들로 매칭시켜준다. key값으로 매치해서 value를 추정
show_info(**p)
print('----------------------------------------------')
# *p -> 값이라고 추정되는 애들로 매칭 but key값으로 출력
show_info(*p)

# * : key
# ** : value

# show_info("홍길동", "도적", 20, "율도국", 180.3)
# 이름: 홍길동 직업: 도적 나이: 20 사는곳: 율도국 키:180

print('----------------------------------------------')

def test(a, b, c):
    print(a, b, c)
# 파라미터 지정해서 실행할수있음
test(c = 30, a = 10, b = 20)
print('----------------------------------------------')

x = [10, 20, 30]

def sumvalue(a,b,c):
    return a + b + c

print(sumvalue(*x)) #60
print('----------------------------------------------')

# 가변인수로 함수 만들 수 있다.
def sumvalue2(*args):
    print("args :", args)

sumvalue2(x)


def show_info2(**kwargs):
    for k, v in kwargs.items():
        print(k, ":", v, sep='')

# show_info2(p)


def show_info3(*args, **kwargs):
    print(*args,":", **kwargs)
show_info3(p)

