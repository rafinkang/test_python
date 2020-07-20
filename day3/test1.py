# 자료형
a = 10
print(type(a))
b = 10.5
print(type(b))
A = 1
print(A, a)

# 10 진법
# bin - 2, oct - 8, hex - 16
print(bin(10), oct(10), hex(10))
print(10, 0b1010, 0o12, 0xa)
print(7+2j, type(7+2j))

# 연산자
v1 = 3 # = 대입연산자
v1 = v2 = v3 = 5 # 뒤에서 부터 대입
# v3 = 5; v2 = v3; v1 = v2; 순으로 대입한것과 같다
a = 10
b = 20
print("a:",a,"b:",b)
# a: 10 b: 20
# 자리바꿈
a, b = b, a
# ??????????????????
print("a:",a,"b:",b)
# a: 20 b: 10
print('-------------------------------------------')
# *b = 남은 값들을 리스트로 받아준다
a, *b = 1, 2, 3, 4, 5
print("a:",a,"b:",b)
# a: 1 b: [2, 3, 4, 5]
*a, b, c = 10, 20, 30, 40, 50
print("a:",a,"b:",b,"c:",c)
# a: [10, 20, 30] b: 40 c: 50


# 출력
print(format(1.2345, '10.2f')) #c
age = 20
print("나는 나이가 "+str(age)+"살 입니다.")
print("나는 나이가 %d살 입니다."%21)
print("나는 나이가 %d살 입니다."%age)
print("나는 나이가 %s살 입니다."%'스무')

print("오늘은 %d월 %d일 이고, %s입니다."%(7,17,'제헌절'))

print("이름은 %s이고 키가 %.2f 입니다."%('강태욱', 184))
print('-------------------------------------------')
print("이름은 {0}, 나이는 {1}".format('뽀로로', 13))
print("이름은 {0}{0}{0}, 나이는 {1}".format('뽀로로', 13))

# 연산자
print(5+3, 5-3, 5*3, 5/3, 5//3, 5%3, divmod(5,3))
print(5**3)
print(5 >= 3, 5 == 3, 5 < 3)
print(5 > 3 and 4< 3 , 5>3 or 4, not(5>3))

print("대"+"한"+"민"+"국")
print("나이: ", str(100), str(5)+'3')
print("만세 "*10)
# 대한민국
# 나이:  100 53
# 만세 만세 만세 만세 만세 만세 만세 만세 만세 만세



print('-------------------------------------------')
a = 5
a = a+1
print(a)
# 6
a += 1
print(a)
# 7
print("부호변경", a, -a, a*-1, -a)
# 부호변경 7 -7 -7 -7

print('boolean : ', bool(0), bool(1), bool(2))
# boolean :  False True True

print(bool(-2), bool(None), bool(''), bool(True), bool(False))
# True False False True False

print('c:\name\python\table')

print('c:/name/python/table')
print('c:\\name\\python\\table')
print(r'c:\name\python\table') # raw data 있는 그대로의 문자로 해석

