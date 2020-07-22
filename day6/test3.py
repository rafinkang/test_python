def add(n1, n2):
    '''
    이거슨 더하기
    '''
    return n1 + n2

def minus(n1, n2):
    '''
    이거슨 빼기
    '''
    return n1 - n2

x = add(100, 200)
y = minus(200,100)
print(x + y) #400

# 두 수의 합을 리턴합니다.
help(add)
# 두 수의 차를 리턴합니다.
help(minus)


def add_minus(n1, n2):
    return n1+n2, n1-n2

x, y = add_minus(300, 100)
print(x, y) 

# i, j = (1, 2)
# i, j = 1, 2
i, j = [1, 2]

# 함수의 리턴 값 : 정수 문자 실수 튜플 리스트 등등...

# def hap(n1, n2, n3=0):
#     return n1+n2+n3

# sumValue = hap(100, 200) # 합계를 리턴합니다... : 300
# print("합계를 리턴합니다... :", sumValue)

# sumValue2 = hap(100, 200, 300)
# print("합계를 리턴합니다... :", sumValue2)


# 가변인수 *n2
def hap(n1, *n2):
    print(n1)
    print(n2)
    # 합계를 구해서 리턴
    # return n1 + sum(n2)
    result = n1
    for i in n2:
        result += i
    
    return result

sumValue = hap(100, 200) # 합계를 리턴합니다... : 300
print("합계를 리턴합니다... :", sumValue)

sumValue2 = hap(100, 200, 300)
print("합계를 리턴합니다... :", sumValue2)

print('------------------------------------------------')

# v = 300
# for k in (100,200):
#     v += k
    
# print(vl)