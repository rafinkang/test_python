import random

# 1. 랜덤 숫자 10개를 입력받는다.
# 2. 이것을 리스트에 담는다
data = list()
for i in range(10):
    num = random.randint(1, 999)
    data.append(num)

# 3. 임시변수를 선언한다.
temp = 0

# 4. 리스트의 모든 요소와 비교해서 큰 값을 임시변수에 담는다.
for i in data:
    if i > temp:
        temp = i

# 5. 최대값을 구해서 출력
print(temp)

# max함수 쓰면 더 편함 ㅋ
print(max(data))

#최소값 구해라
temp = 1000
for i in data:
    if i < temp:
        temp = i

print(temp)

# min쓰면 더 편함 ㅋ
print(min(data))