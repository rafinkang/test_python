import random

for i in range(10):
    print(random.random()) # 0~1 사이의 실수값

for i in range(100):
    print(random.randint(1,6)) # 1~6 사이 정수값

# SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 순서 ㅇ, 중복 ㅇ
cnt = int(input("몇번 : "))
for k in range(cnt):
    m = list(range(1,46)) 
    # print(m)

    # 랜덤하게 두개의 값을 출력
    # a = random.randint(0, 44)
    # b = random.randint(0, 44)
    # print("m[", a ,"] : ", m[a] ,", m[", b ,"] : ", m[b])

    # m[a], m[b] = m[b], m[a]
    # print("m[", a ,"] : ", m[a] ,", m[", b ,"] : ", m[b])

    # m리스트의 요소중 1개를 랜덤하게 뽑아 출력하고자 한다.
    # print(m[random.randint(0, len(m))])

    for i in range(1000):
        a = random.randint(0, 44)
        b = random.randint(0, 44)
        # print("m[", a ,"] : ", m[a] ,", m[", b ,"] : ", m[b])
        m[a], m[b] = m[b], m[a]
        # print("m[", a ,"] : ", m[a] ,", m[", b ,"] : ", m[b])

    # lotto
    lotto = []
    for j in range(6):
        lotto.append(m[j])
        # print(m[j], end ='\t')

    lotto.sort()
    for l in lotto:
        print(l, end="\t")
    print()

# ---------------------------------------------------------


    