# 예외란? 프로그램 실행 중 발생한 예상치 못한 오류 : 가벼운 오류
# 예외를 처리 해줄 수 있다.
'''
case by case
1.
try:
    문장1
    문장2
except ????:
    예외처리문장1
    예외처리문장2
except ????:
    예외처리문장3

'''

import random

# 사용자 정의 에러 raise 로 발생시킨다
class EvenError(Exception):
    pass


# 0~9 사이의 정수를 랜덤하게 생성
try:
    n = int(input("숫자입력 : "))
    # 사용자가 입력한 값이 짝수이면 실행안함
    if n % 2 == 0:
        raise EvenError

    for i in range(10):
        a = random.randint(0,9)
        print(n/a)

except EvenError:
    print("짝수는 계산 안해줘..")

except ZeroDivisionError:
    print("0으로 나눌 수 없음.")

except ValueError:
    print("숫자만 입력하세요")