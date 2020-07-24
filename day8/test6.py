'''
    정규표현식(regular expression) : 일정한 규칙(패턴)을 가진 문자열을 표현하는 방법
'''
import re
# re.match('패턴', '문자열')

print(re.match('Hello', 'Hello Python world'))

print('Hello Python world'.find('Hello'))

# 첫글자가 H로 시작?
# ^H - 첫글자
print(re.search('^H', 'Hello Python world'))
# d$ - 마지막글자
print(re.search('world$', 'Hello Python world'))

print('--------------------------------------------------')
# 010-1234-5678
print(re.match('[0-9]+', '1234')) # + 1개 이상
print(re.match('[0-9]*', '1234')) # * 0개 이상

# 
# aaabbb ==> a가 1개 이상 있나 ?

print(re.match('a+b', 'aaabbb'))
print(re.match('가-힣+','q불금달료보자.'))
# + : 1개이상 , *: - 0개이상 , ? : 0 or 1