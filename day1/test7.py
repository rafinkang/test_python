'''
숫자형 변수
정수형 (Integer) ==> int
실수형 (Float) 3.14 ==> 
복소수 (Complex) 1.3 + 1.9i(j) ==>

동적타이핑 언어 - 할당하는 순간 자료형이 정해지는 언어
type(a) - 자료형 확인

'''

a = 10
b = 3.14
c = 1.9j

print(type(a), type(b), type(c))
# <class 'int'> <class 'float'> <class 'complex'>

b = 20
print(type(b), b);

c = "10"

# 형변환 함수 : int(), float(), complex(), str()

print("a : " + str(a))
print("b : " + str(b))
print("c : " + c)

# a = 10, b = 20
# 치환
# b = 10, a = 20

# 1. 임시변수를 만든다
# 2. 첫번째 변수를 임시변수에 담는다.
temp = a
# 3. 두번째 변수의 값을 첫번째 변수에 담는다.
a = b
# 4. 임시변수의 값을 두번째 변수에 담는다.
b = temp
# 5. 끝~~

# 파이썬에서 치환/ ? ? ?
a, b = b, a

x = 10
y = 10
z = 10
print('x',x,'y',y,'z',z)

x = y = z = 20
print('x',x,'y',y,'z',z)

# 아무것도 없는 값
x = None # 다른 언어들은 null 
print(x)

a = 100 # a에 100을 대입
# 20을 증가시킨 후 출력
a += 20 # a = a + 20
print(a)


