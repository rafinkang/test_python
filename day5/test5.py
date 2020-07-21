import random

# dict - 키 : 벨류 의 쌍으로 이루어짐, 순서 X
# 키와 값으로 매핑되어 있는 순서가 없는 집합
# JSON

mydic = dict(k1 = 2, k2 = 'abc', k3 = 3.4)
print(mydic)

dic = {'파이썬' : '뱀', '자바' : '커피', '오라클' : '예언자'}
print(dic, len(dic))
dic['스미스'] = "백그라운드프로세스"
print(dic, len(dic))
dic['neo'] = "주인공"
dic['스미스'] = "bg"
print(dic, len(dic))
# dic.clear()
# print(dic, len(dic))
print("----------------------------------")
for key in dic:
    print(key, dic[key])

print("----------------------------------")
# 처음부터 value들만 출력
for val in dic.values():
    print(val)

print("----------------------------------")
# 둘다 가져오기
for key, val in dic.items():
    print("key : " + key + ", value : " + val)

print("----------------------------------")
# 키가 있는지 여부 판단 : in
print('neo' in dic)
# neo 삭제
del dic['neo']
print(dic)
print("----------------------------------")

dic['game'] = ['대항해시대', '바람의나라', '문명6', '토탈워']
print(dic)
dic['broadcasting_co'] = ['kbs', 'mbc', 'sbs', 'ytn', 'jtbc']

# JSON 풀어서 보여주는거
from pprint import pprint as pp
pp(dic)


# 1부터 100사이의 정수를 생성
num = random.randint(1,100)

# 사용자로부터 숫자 한개를 입력

# 두수가 일치하면 일치합니다. 메세지 출력
# 일치하지 않으면 일치하지 않습니다 메세지 출력
# else: print("일치하지 않습니다.")

# 일치하지 않으면 사용자가 입력한 수 보다 큰지 작은지 출력
# 다시 입력 받도록 하고싶다

# def aaa() :
#     guess = int(input("숫자 한개 입력해라 : "))
#     if num == guess : print("일치합니다.")
#     else : 
#         if num > guess:
#             print('그거보단 클걸?')
#         else:
#             print('그거보단 작을걸?')
#         aaa()

# # aaa()

# while True:
#     guess = int(input("숫자 한개 입력해라 : "))
#     if num == guess : 
#         print("일치합니다.")
#         break
#     else : 
#         if num > guess:
#             print('그거보단 클걸?')
#         else:
#             print('그거보단 작을걸?')


# 과일명, 과일생산지를 dictionary 로 작성
fruit = {
    '사과' : '여기',
    '딸기' : '저기',
    '포도' : '포도당',
    '배' : 'ㅡㅡ',
    '망고' : '구아바',
}
print(fruit)