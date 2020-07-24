# 1.
# 	다음을 람다식으로 수정하세요 

# 	def test(x):
# 	     return x+10
print((lambda x : x + 10)(10))
print('-----------------------------------------------')
# 2. 	
# "Yeah 다시 돌아왔지 내 이름 레인(RAIN) 스웩을 뽐내 WHOO! They call it! 왕의 귀환 후배들 바빠지는 중! 신발끈 꽉 매고 스케줄 All Day 내 매니저 전화기는 조용할 일이 없네 WHOO! "
# 문자열중 공백을 기준으로 몇글짜씩인지 알아 내려고한다. 파이썬 코드로 작성하세요 
msg = "Yeah 다시 돌아왔지 내 이름 레인(RAIN) 스웩을 뽐내 WHOO! They call it! 왕의 귀환 후배들 바빠지는 중! 신발끈 꽉 매고 스케줄 All Day 내 매니저 전화기는 조용할 일이 없네 WHOO! "
rain_list = msg.split()
print(rain_list)

print('-----------------------------------------------')
# 3. 
# 2번 문자열중 글자가 4자이상인 단어만 출력하세요 
for i in rain_list:
    if len(i) >= 4:
        print(i)

print('-----------------------------------------------')

[print(i) for i in rain_list if len(i) >= 4]

print('-----------------------------------------------')
# 4. 	도명: 도청소재지 로 만들어진 dictionary 가 있다. 
do_city  = { "경기도":"수원", "강원도":"춘천"}
# dictionary 내포 표현식으로 출력 하세요 

[print(k,":",v) for k, v in do_city.items()]

print('-----------------------------------------------')
# 5. 지역변수와 전역변수의 차이점? 
'''
전역변수 : global, 내부 함수들에서도 호출해서 사용 가능
지역변수 : 선언된 지역(함수) 안에서만 존재하는 변수. 외부로 못나감
'''

# 6..
# 	다음 코드를 실행한후에 화면에 출력 되는 a의 값은 얼마인가? 
# 	왜 차이가 날까요? 	
'''
a  = 100 
def show():
    a = 200
    b = 100
    print(a)  ==> 200 show()내 지역변수a 를 출력
show()
print(a)  ==> 100 전역변수 a를 출력

'''

# 7. 
# a  = 100 
# 	def show():
# 	    ____________________
# 	    a = 200
# 	    b = 100
# 	show()
# 	print(a) 
# 	200 으로 출력되게 해주려고한다. ___global a____ 들어갈 코드는 ? 
a  = 100 
def show():
    global a
    a = 200
    b = 100
    
show()
print(a) 
print('-----------------------------------------------')
# 8. 
# 	지역변수의 목록을 확인하려면 어떤 명령을 사용할까? 
# 확인 할 지역 내에서 locals()
print(locals())
print('-----------------------------------------------')
# 9.

# 	def fx():
# 	    data1  = 500    
# 	    def fx2():   
# 	        _____________________
# 	        data1 = 300  
# 	    fx2()
# 	    print(data1)
# 	fx()

# 	이 코드를 실행했을때 화면에 어떤값이 출력될까? 
#   500

# 10.
# 	출력 결과를 300 이 나오게 하려면 __________ 에 알맞은 코드는?  nonlocal data1
def fx():
    data1  = 500    
    def fx2():   
        nonlocal data1
        data1 = 300  
    fx2()
    print(data1)
fx()
print('-----------------------------------------------')

# 11.
# 	일급함수의 특징 3가지를 정리하세요
'''
1. 함수를 다른 함수의 인수로 전달할 수 있다.
2. 반환값으로 함수를 사용할 수 있다.
3. 변수에 저장할 수 있다.
'''
# 12.
# 	def  tax():
# 	    a = 1.1
# 	    def cal(b):
# 	        return a*b
# 	 return cal
	
# 	getTax = tax()
# 	print(getTax(1000))   # 출력결과는 ? 1100.0
def  tax():
    a = 1.1
    def cal(b):
        return a*b
    return cal

getTax = tax()
print(getTax(1000))   # 출력결과는 ? 1100.0

print('-----------------------------------------------')
# 13.

# 	12번에서 cal 함수는 getTax 함수 호출할때 다시 꺼내서 사용되어지는데 
# 	이런 함수를 ____클로져Closure_____ 라고 한다. 

# 14. 
# 	일정한 규칙(패턴)을 가진 문자열을 표현하는 방법  _______정규표현식_______ 이라 한다.

# 15. 
# 	사용순서 
# 		1. import re 
# 		2. re.compile('패턴')
# 		3.  pattern.match()     :문자열의 처음부터 비교
#           pattern.search()    :문자열 전체 검색
#           pattern.findall()   :패턴에 맞는 모든 문자열을 리스트로 반환
#           pattern.finditer()  :패턴에 맞는 모든 문자열을 오브젝트로 반환
		
# 16.
	
# 	"Hello Python  Oracle  Friday 010-1234-5678  2020년 7월 24일 " 
msg = "Hello Python  Oracle  Friday 010-1234-5678  2020년 7월 24일 " 
# 	문자열중 전화번호만 찾아서 출력하고자한다. 
# 	파이썬 코드로 작성하시오.

msg_list = msg.split()
for i in msg_list:
    if len(i.split('-')) > 1:
        print(i)

print('-----------------------------------------------')
# 17.
# 	16번 문제를 정규표현식으로 작성하시오 
import re
pattern = re.compile("\d{3}-\d{3,4}-\d{4}")
print(pattern.search(msg))
		
	
	