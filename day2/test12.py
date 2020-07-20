# 문자열

name = "my name is KS"

print(name)

sorry = "I'm sorry"
print(sorry)

hobby = " cyber \t fishing"
print(hobby)

print('-------------------------------')

# 5개의 정수형 변수에 10 20 30 40 50 값을 대입
val1, val2, val3, val4, val5 = 10, 20, 30, 40, 50
# 출력
print(val1, val2, val3, val4, val5)


# 리스트
# 목록 : [] 대괄호로 묶어 준다. 각각의 값을 Element 
# element 의 구분은 , 로 한다.
a = [10, 20, 30, 40, 50]
print(a)
print(a[0])
# 40을 출력
print(a[3])

# 빈 리스트 작성
m = []
# 연속된 값 만들기 - range(시작값, 끝값, 증가값)
print(range(0, 10))
m = list(range(0,10))
print(m)

# 10부터 19까지 10개의 연속된 숫자로 된 k list를 만들고 화면에 출력해보세요
k = list(range(10,20,2))
# 화면에 출력
print(k)

print(list(range(100,0,-1)))

# 1부터 1000 사이의 3의 배수를 목록으로 출력
print(list(range(3, 1000, 3)))

# 달의 표면온도는 밤: -170 낮: 120 초당 3도씩 상승한다고 가정했을때 온도의 변화를 리스트로 맨들어ㅓ
print(list(range(-170, 120, 3)))
