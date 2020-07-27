# 1. 두 개의 정수 값을 받아 두 값의 평균을 구하는 함수를 작성하고 임의의 값으로 실행 하세요 
def avg(a, b):
    return (a+b)/2





# 2. sList 는 학생들의 영어 점수로 만든 리스트 이다.  최댓값과 최솟값을 반환하는 함수를 작성하세요.

sList = [ 90, 80, 23, 55, 32, 50, 95, 90, 85, 60, 75, 35, 88, 92]

def max_min(listData):
    return max(listData), min(listData)


# 3. e:/dev/python_workspace/  경로에 있는 *.txt 파일의 목록을 파이썬 리스트로 반환하는 함수를 작성하세요.

import os

def get_list(path):
    result_list = []
    for file in os.listdir(path):
        if file.endswith('txt'):
            result_list.append(file)
    return result_list



# 4. 오늘의 월 일을 출력하는 함수를 작성하세요 
import time

def get_todate():
    # ti = time.ctime().split()
    # return ti[1] +" "+ti[2]
    ti = time.localtime()   #현재 시간
    timeToString = time.strftime('%m월 %d일', ti)   #현재시간 dateformat적용
    return timeToString





# 5.  다음 함수를 작성하세요 

def get_triangle_area(width, height):
    return int(width * height / 2)



# 6. 

import math
def get_circle_area(radius):
    return math.pi * radius**2





# 7. nList 에 랜덤하게 1부터 100사이 의 정수 20개 를 넣는다. 
import random
nList = []
for i in range(20):
    nList.append(random.randint(1,100))
# 8. nList에 홀수 가 몇개가 있는지 를 리턴하는 함수를 구하세요 
def get_odd(listData):
    odd = 0
    for i in listData:
        if i%2 == 1:
            odd += 1
    return odd

# 9.  5자로 구성된 랜덤문자를 만들어 20개를 넣는다. 소문자   : 97~122
wordList = []   # wordList = ['abcde', 'xwdsd, ....]
for i in range(20):
    word = ''
    for j in range(5):
        word += chr(random.randint(97,122))
    wordList.append(word)

# 10. wordList 요소에서 뒤에 3글자만 자른 문자를 갖는 리스트를 출력하는 함수를 작성하세요
def get_last_word(listData):
    result = []
    for i in listData:
        result.append(i[-3:])
    return result

# 11. 지금까지 만들어진 함수를 test 라는 모듈로 작성하세요
# 파일명 변경 test.py

# 12. 현재 파일에서 실행할때만 테스트 결과가 출력되게 작성하세요 
# 맨 아랫줄

# 13. ex1.py 파일을 작성하고  test. get_circle_area(300)을 실행시켜보세요

# 14. 다른 모듈의 함수를 불러 사용하는 방법 3가지를 정리하세요 
'''
import 모듈명 
from 모듈명 import 함수명
from 모듈명 import *
'''

if __name__ == "__main__":
    print(avg(200,100))
    print('----------------------------------------------------------')
    print(get_last_word(wordList))  #  [ cde ,  dsd  , .... ]
    print('----------------------------------------------------------')
    print(wordList)
    print('----------------------------------------------------------')
    print(get_odd(nList))  # n
    print('----------------------------------------------------------')
    print(nList)
    print('----------------------------------------------------------')
    print(get_circle_area(10))  # 314.1592653589793
    print('----------------------------------------------------------')
    print(get_triangle_area(100,200))  # 10000
    print('----------------------------------------------------------')
    print(get_todate())   # 7월 27일 
    print('----------------------------------------------------------')
    print(get_list('e:/dev/python_workspace/'))
    print('----------------------------------------------------------')
    print(max_min(sList))
    print('----------------------------------------------------------')