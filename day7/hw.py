# 1. 
# 	변수명규칙?
'''
    영문자(대,소문자 구분), 숫자, 언더바를 사용할 수 있다.
    첫 자리에는 숫자를 사용할 수 없다.
    파이썬 키워드는 변수 명으로 사용할 수 없다.    
'''

# 2. 
# 	제곱값을 리턴하는 함수를 작성하시요 
# 	print(square(5)) # 5
 
def square(n):
    return n*n
print(square(5)) # 5
print('-------------------------------------------------------------')

# 3. 
# 	2번의 결과를 이름이 없는 익명함수(람다함수)로 작성하시오 
print((lambda x: x*x)(5))
print('-------------------------------------------------------------')

# 4. 

# 	1부터 100까지 값을 가지고 있는 리스트가 있다. 
# 	m = [1,2, ... 100]

# 	각 리스트의 값을 3배로 만드는 함수 triple을 작성하시오 
m = []
for i in range(1,101):
    m.append(i)
# print(m)
def triple(list):
    result = []
    for i in list:
        result.append(i*3)
    return result

print(triple(m))
print('-------------------------------------------------------------')
# 5. 

# 	람다식을 사용해서 4번과 동일한 결과를 출력하세요 

print(list(map(lambda i: i*3,m)))
print('-------------------------------------------------------------')

# 6.
	
# 10칸 짜리 정수형 리스트 rnd 에 랜덤(100이하, 중복되지않는)하게 값을 할당하고
# 	최대값 , 최소값을 출력해보자. (내장함수 사용) 
import random
rnd = []
while len(rnd) < 10:
    rnd.append(random.randint(1,100))
    list(set(rnd))

print(rnd, max(rnd), min(rnd))
print('-------------------------------------------------------------')

# 7. 	
# 	1부터 100까지 정수를 순서대로 가지고 있는 리스트(k)를 생성 하세요 
k = []
for i in range(1, 101):
    k.append(i)
print(k)
print('-------------------------------------------------------------')
# 8. 
# 	7번을 리스트 내포 표현식으로 코드를 수정하세요 
k2 = [i for i in range(1, 101)]
print(k2)

print('-------------------------------------------------------------')
# 9. 
# 	8번에서 짝수만 남기게 조건을 추가해 보세요 

k3 = [i for i in range(1, 101) if i%2==0]
print(k3)

