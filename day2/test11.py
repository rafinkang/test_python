print(1+1) # int형
a = 10
print(a)
a = float(a) # float형
print(a)
print(complex(1.3, 1.4j)) # 복소수-

print('--------------------------------------------')
# x = input("아무 값이나 하나 입력하세요.")
# print("x의 값은 :", x)

# 문자열 : "", '', ''' ''', """ """

print(3>5) # True/False로 값 리턴

a = 100
b = 200
print(a<b)

c = None
print(c)
# 
print(100>2 and 300>100)
print(100>2 and 300>100 or 100>200)

x = True
y = False

print(x and y)
print('--------------------------------------------')

print(True and True)
print(False or True)
print (not True)

a = 300
b = 200
print(a == b)
print(a != b)


# 국어, 영어, 수학 점수를 입력받기
# 60점 이하가 있다면 False, 아니면 True

kor, eng, mat = input("국어, 영어, 수학 점수를 입력").split(',')
kor, eng, mat = int(kor), int(eng), int(mat)

print(kor >= 40 and eng >= 40 and mat >= 40)
print("평균 :", (kor+eng+mat)/3 >= 60)