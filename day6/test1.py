# function : 함수
# 반복되는 코드를 줄여주기 위해 특정 코드에 이름을 부여해놓은 것
# 내장함수

# def 함수명(parameter=매개변수,...):
#     실행할 코드
#     [retuen 결과값]

# 함수명(arguement=인수)

print('111111111111')
def double(x):
    print('222222222')
    return x*2
print('333333333')

# 불러서 실행 : 호출
y = double(10)
print(y)

k = double(20)
print(k)

print('------------------------------')
# 로또번호 생성기
import random

def getLotto(no):
    lottoList = []
    for i in range(no):
        lotto = []
        while len(lotto) < 6:    
            # 1. 랜덤하게 1~45사이 정수를 뽑는다
            num = random.randint(1,45)
            # num in lotto -> num 이 lotto라는 리스트에 존재하면 True / False
            if num in lotto:
                # 3. 중복된 값이 있으면 다시 뽑는다.
                continue
            else:
                # 2. 로또 리스트 담는다
                lotto.append(num)
                
            '''
                lotto.append(num)
                for i in range(0, len(lotto)-1):
                    if lotto[i] == num :
                        lotto.pop()
            '''
    # 4. 6자리 모두 완성되면
    # 5. 정렬한다.
        lotto.sort()
        # lotto.reverse() #역순 파이써ㄴ은 체인블록 안되는듯
        lottoList.append(lotto)

# 6. 출력한다.
    return lottoList;


print("이번주 대박 로또 번호!!! :", getLotto(3))