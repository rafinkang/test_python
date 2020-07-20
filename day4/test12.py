# while True:
#     value = int(input("숫자를 입력 : "))
#     # 5의 배수인가요?
#     if value%5 == 0 :
#         continue # 여기까지 하고 앞으로 넘어감
#     print(str(value) + "는 5의 배수가 아닙니다.")

# print("이제 그만~~~")

# 1부터 100까지 수중 3의 배수 5개만 출력

# 5개 채워지면 break;
cnt = 0
for i in range(1,101):
    if i%3 == 0:
        print(i)
        cnt += 1
    if cnt == 5: break

print('------------------------------------')
# 출력은 같지만 100번 다 돈다
cnt = 0
for i in range(1,101):
    if i%3 == 0 and cnt < 5:
        print(i)
        cnt += 1

print('------------------------------------')
# 얘도 뭐 비슷한데 쓰기 구림
cnt = 0
num = 1
while num <= 100:
    if num%3 == 0:
        print(num)
        cnt += 1
    if cnt == 5: break
    num += 1    