# built-in function - 내장함수

# sum :  합
print(sum([10,20,30]), sum((10,20)), sum({2,3}))
# bin : 2진수
print(bin(0))
# int float str
print(int(2.7), float(3), str(5))

a = 10
b = a + 5
print(b)

print(round(1.2), round(1.6))
print('---------------------------------------------------------')

import  math

print(math.ceil(1.2), math.ceil(1.6)) #정수 근사치중 큰수
print(math.floor(1.2), math.floor(1.6)) #정수 근사치중 작은수

print('---------------------------------------------------------')

bList = [True, 1, False]

print(all(bList)) # True and 1 and False
print(any(bList)) # True or 1 or False t



def do1():
    print("첫번째 함수 실행중")
def do2():
    print("두번째 함수 실행중")
def do3():
    print("세번째 함수 실행중")
    do1()
    do2()
    print("세번째 함수 끝")

do3()
print('---------------------------------------------------------')

# 재귀적 함수 호출
def sayHello(cnt):
    cnt -= 1
    print("Hello~~~~")
    if cnt > 0:
        sayHello(cnt)
sayHello(5)

print('---------------------------------------------------------')
# factorial

# def factorial(num):
#     res = 1
#     for i in range(1, num+1):
#         res *= i
#     return res

def factorial(num):
    if num==1: 
        return 1
    return num*factorial(num-1)

print(factorial(5)) # 120

# 1 1 2 3 5 8 13 21 ...
def fibonacchi(n):
    if n <= 1:
        return n
    return fibonacchi(n-1) + fibonacchi(n-2)

print(fibonacchi(10))

for i in range(10):
    print(fibonacchi(i), end=" ")