'''
자료형 : 

'''
# 문자열.find('찾을문자열', start, end) return start에서~end 사이의 값 중 찾은 문자의 index
s = 'sequence'
print(s, len(s), s.count('e'), s.find('e'))
print(s.find('e', 3), s.rfind('e'))

ss = 'mbc'
print('mbc', type(ss), id(ss))

print('문자열 자르기')
print(s, s[2:4], s[:3], s[3:], s[3::2])

# 문자열공백제거
msg = " Hello Python "
print(msg)
print(msg.strip())
print(msg.rstrip()+"^^")
print(msg.lstrip())

msg = " 구정,신정,크리스마스,초파일,추석"
# m 리스트
m = list(msg.split(','))
# 반복출력
for i in m:
    print(i)

msg3 = list('hello')
print(msg3)

str_time = ['10','44','30']
print(":".join(str_time))

# 문자열을 , 단위로 짤라서 리스트 == > split(",")
# 리스트에 , 문자를 붙여서 문장열로 ==> ",".join(리스트)

msg3 = list('hello')
print(msg3)

print(msg3[4])
msg3[0] = 'm'
print(msg3)