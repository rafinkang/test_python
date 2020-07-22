import math
print(math.factorial(5))

# 위아래 동일

def factorial(no):
    result = 1
    for i in range(no, 1, -1):
        result = result * i
    return result

print(factorial(3)) # 3! ==> 3*2*1

print(factorial(5)) # 5! ==> 5*4*3*2*1

# 5 * 4 * 3 * 2 * 1 = 120 형식으로 출력하는 factorial2() 함수를 정의하세요.

def factorial2(no):
    '''
    # 심심해서 만든 함수우
    '''
    value = 1
    result = ''
    for i in range(no, 1, -1):
        value = value * i
        result = result + str(i) + ' * '
    return result+'1 = '+ str(value)

print(factorial2(7)) # 3! ==> 3*2*1
print(factorial2.__doc__)
    
print("---------------------------------------")

help(factorial2)