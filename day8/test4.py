# 파이썬의 함수는 모두 일급 함수
# 함수를 다른 함수의 인수로 전달할 수 있다.
# 반환값으로 함수를 사용할 수 있다.
# 변수에 저장할 수 있다.

def add(a,b):
    return a+b
# print(add(100,200))

# 변수에 함수 넣기
plus = add
print(plus(100,200))

# 파라미터에 함수넣기
def appendFunction(f1, c, d):
    return f1(c,d)

print(appendFunction(add,1000,2000))