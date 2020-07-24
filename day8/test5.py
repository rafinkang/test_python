# 함수를 호출할 때 다시 꺼내서 사용하는 함수 : 클로져(Closure)

def plus_ten():
    a = 3
    def add(b):
        return b+a
    return add

cal = plus_ten()
print(cal(1))


def plus_ten2():
    a = 10
    return lambda b: a+b

cal2 = plus_ten2()

print(cal2(100), cal2(200))