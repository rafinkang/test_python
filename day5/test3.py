import random
# 가위 바위 보
print("1. 가위 2. 바위 3. 보 ")
userInput = int(input("가위 바위 보 중 선택하세요 : "))
userInput -= 1
# 가위 바위 보라는 글자를 가진 리스트를 선언
li = ['가위', '바위', '보']
 
# 0, 1, 2중 하나를 리턴하는 랜덤인트 함수 사용
idx = random.randint(0,2)
# 출력: 리스트[x]
# print(li[idx])

# 승부판정
# 사용자 입력값, 컴퓨터의 랜덤 값의 차 를 비교
print("사용자 입력값 : ", userInput, li[userInput])
print("컴퓨터 입력값 : ", idx, li[idx])
print("차이값 : ", userInput-idx)

# 차이값 : 0 이면 : 비김
# 1 이거나 -2이면 : 사용자 승
# -1이거나 2 이면 : 컴퓨터 승
asdf = userInput-idx

if asdf == 0:
    print("비겼습니다.")
elif asdf == 1 or asdf == -2:
    print("사용자 승!")
else:
    print("컴퓨터 승!")