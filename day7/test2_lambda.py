mList = [1000,2000,3000,4000,5000]

# for문 사용해서
# for i in range(len(mList)):
#     mList[i] = int(mList[i]*1.1)


# print(mList)
# 리스트 내포 표현식 : List Comprehension
# 리스트 내부에 반복문/조건문의 축약형 형태 전달 가능
# [리턴값 for i in 대상]
# [리턴값 for i in 대상 if 조건]

print([int(i * 1.1) for i in mList])


list2 = [-5, -2, -1, 0, 2, -3, -2, 10, 3]
# 1월 어느날 최고온도
# 영상인 날짜의 온도만 리스트로 작성하려고 한다.
list3 = []
for i in list2:
    if i >= 0:
        list3.append(i)

print(list3)

def test(x):
    return x+1
print(test(100))

# lambda 함수 (익명함수)
# 이름이 없는 함수
# 코드가 간결, 메모리가 절약

print((lambda x : x + 1)(100))

# 자리바꿈 해주는 함수

def plusData(a, b):
    return a + b

c = 100
d = 100
print(c, d)
k =plusData(c,d)

print(type(plusData), id(plusData))
pd = plusData
print(id(plusData), id(pd))



# 람다식
print((lambda a, b : a+b)(100, 200))
print('--------------------------------------')

lamdd = lambda a, b : a+b
lamdd(1000, 2000)

print('--------------조건식을 사용한------------------------')
print((lambda a, b: a if a%2==0 else b)(11,20))

