
def do_test(*k):
    v = 0
    for i in k:
        v += i
    print(v)
    return v

# 리턴값이 있는 함수는
x = do_test(300,100,200,300)


def do_test1(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

do_test1(name="홍길동", age=20)