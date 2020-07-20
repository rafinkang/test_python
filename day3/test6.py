# 제어문
# 조건 분기문
# 주어진 조건 발생하면 다른 문장이 실행되게 처리
# if condition:
#     pass
# elif:
#     pass
# else:
#     pass

# 사용자로 부터 성적입력받기
# score = int(input("당신의 성적을 입력하세요: "))
# print(score >= 90)
# if score >= 90:
#     print("당신의 성적은", score, "입니다. A학점!")
# elif score >= 80:
#     print("당신의 성적은", score, "입니다. B학점!")
# elif score >= 70:
#     print("당신의 성적은", score, "입니다. C학점!")
# elif score >= 60:
#     print("당신의 성적은", score, "입니다. D학점!")
# else:
#     print("당신의 성적은", score, "입니다. F학점!")

# 1부터 20까지 값을 출력
# 1. 1 2 3 4 5 6 7 .. 20
for i in range(1,21):
    print(i, end=" ")
print()
print('------------------------------------')
# 2. 홀수만 출력(if)
for i in range(1,21):
    if(i%2):
        print(i, end=" ")
print(list(range(1,21)))
print('------------------------------------')

# 구구단 5단 출력
# 5 * 1 = 5
# 5 * 2 = ****
# 5 * 3 = 15
for i in range(1,10):
    if(i%2):
        print('5 *',i,'=',5*i)
    else:
        print('5 *',i,'= ****')
        