# a : 100, b: 200, c: 300
# 값 교환
# a : 300, b: 100, c: 200
# 각변수에서 10씩 증가
# a : 310, b: 110, c:210

a, b, c = 100, 200, 300

print('a :', a, 'b :', b, 'c :', c)

a, b, c = c, a, b
print('a :', a, 'b :', b, 'c :', c)

a += 10
b += 10
c += 10
print('a :', a, 'b :', b, 'c :', c)

print('----------------------------------------')
# 사칙연산
a, b = 10, 20
print(a+b)
print(a-b)
print(a*b)
print(a/b) # int 연산 int -> int 0.5
# print(a//b) # int/int=>int 정수형/정수형 -> 정수로만 리턴
print(a%b) # 나머지
a = -a
print(a)
print('----------------------------------------')

# msg = input(" 출력할 메세지를 입력하세요. ")
# print(msg)

# 사용자로 부터 두 수를 입력받아 화면에 출력

input1 = input("1번 값을 입력하세요.")
input2 = input("2번 값을 입력하세요.")

print("두 수의 합은", int(input1) + int(input2), "입니다.")
