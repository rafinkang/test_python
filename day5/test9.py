'''
    함수 : 여러개의 실행문을 하나의 묶음으로 만든 실행단위

    내장함수 : 설치후에 포함되어있는 함수

    사용자 정의 함수 : 사용자가 정의한거;;
        def funcname(parameter_list):
            pass
            [return 반환값]
'''

# *
# **
# ***
# ****
# *****
# for n in range(1,6):
#     print("*"*n)

def printStar(num) : 
    for n in range(1,num+1):
        print("*"*n)
        
printStar(5)
print('-----------------------------------')
# 구구단 3단 출력
# for i in range(1,10):
#     print(3,"*",i,"=",3*i)

def gugudan(dan) : 
    for i in range(1, 10):
        print(dan,"*",i,"=",dan*i)

gugudan(3)
print('-----------------------------------')

# 1부터 지정한 숫자까지 누적된 값을 출력하는 함수
def hap(num) :
    value = 0
    for i in range(1, num+1):
        value += i
    print("1부터 "+ str(num) +"까지의 합은" +str(value))
    # 지금 계산한 값을 날 호출(실행)한 코드에 전달하고 싶다.
    return value;

print(hap(100))

x = hap(50)
y = hap(100)
print(x+y)
print('-----------------------------------')


# odd(숫자) 1부터 해당 숫자까지의 홀수의 누적합

def odd(num, no):
    value = 0
    for i in range(1, num+1):
        if i%no == 0 : 
            value += i
    return value

a = odd(100, 10)
b = odd(30, 3)
print(a, b, a+b)


