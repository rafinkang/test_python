
# 과일명, 과일생산지를 dictionary 로 작성
fruit = {
    '딸기' : ['논산', '하우스'],
    '망고' : '필리핀',
    '두리안' : '말레이시아',
    '사과' : ['충주','영주'],
    '배' : '나주',
}
# print(fruit)

# 딸기 생산지를 출력
print(fruit['딸기'])
# 망고 생산지를 출력
print(fruit['망고'])
# 과일명:생산지 형식으로 전체 출력
for key, val in fruit.items():
    print(key, val)