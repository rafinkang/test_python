import re

# re.compile(pattern: AnyStr, flags: Union[int, RegexFlag]) -> Pattern[AnyStr]
p = re.compile('[A-z]+')
print(p, type(p))
# 패턴 : 정규식을 컴파일 한 결과

# 문자열 검색
# match()   : 문자열의 처음부터 정규식과 매치되는지 조사
# search()  : 문자열 전체를 검색하여 정규식과 매치되는지 조사
# findall() : 정규식과 매치되는 모든 문자열을 리스트로 돌려준다.
# finditer(): 정규식과 매치되는 모든 문자열을 반복가능한 객체로 돌려준다.

m = p.match("regular expression")
print(m)

if m:
    print(m.group())
else:
    print("no match")
print('------------------------------------')
result = p.search("999999999 aaaaaabbbbb")
# <re.Match object; span=(10, 21), match='aaaaaabbbbb'>
print(result)

print('------------------------------------')
result2 = p.findall("hello python world today is monday")
# ['hello', 'python', 'world', 'today', 'is', 'monday']
print(result2)

# for문으로 1개씩 출력
for data in result2:
    print(data)

print('------------------------------------')

result3 = p.finditer("today is monday Life is a blow")
print(result3)                              #<callable_iterator object at 0x03A11FB8>
for data in result3:
    print(data)                             #<re.Match object; span=(26, 30), match='blow'>
    print(data.group())                     #blow
    print(data.start(), ":", data.end())    #26 : 30

print('------------------------------------')

msg = " 999,999 smartphone bbb@naver.com aaa@gmail.com"

print(re.findall('[a-zA-Z0-9]+@+[a-zA-Z0-9]+.[a-zA-Z0-9]+', msg))
p_email = re.compile("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$")
# 이메일만 선택해서 출력
result4 = p_email.findall(msg)
print(result4)

for email in result4:
    print(email)