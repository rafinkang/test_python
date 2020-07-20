# 튜플 (Tuple)
# list와 비슷하지만 한번 생성되면 값을 변경 할 수 없다.
# 불변한 순서가 있는 객체의 집합이다.
a = ( 10, 20, 30, 40, 50)
print(a[0])

b = tuple(range(5,10))
print(b)
print(b[2])

# b[2] = 100 튜플은 값의 수정이 되지 않는다.

print(len(a)) # length 함수

# 제어문
# 문장의 흐름을 제어해주는 명령

# for 변수 in 자료형:
#     반복할 명령

for i in a:
    print(i)
print("test------------------------------")

# 1부터 20까지 화면에 출력
# 1.프린트문으로 출력
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)
print(11)
print(12)
print(13)
print(14)
print(15)
print(16)
print(17)
print(18)
print(19)
print(20)

print("------------------------------")
# 2.for문
for i in range(1,21):
    print(i)

print("------------------------------")
# 반복문 사요앻서 구구단 3단 출력
for i in range(3,30,3):
    print(i)
print("------------------------------")
for i in range(1, 10):
    print('3 *',i,'=',3*i)



print("------------------------------")
# 1부터 10까지 누적합을 출력

# 1, 1부터 10까지 값을 화면에 출력한다.
# print(1); print(2); print(3); print(4); print(5); print(6); print(7); print(8); print(9); print(10); 
# d = list(range(1,11))
# for i in d:
#     print(i);
for i in range(1,11):
    print(i);

# 2. 누적합을 담을 변수를 선언한다.
sum = 0
# 3. 출력하기전에 1씩 증가하는 값을 누적용변수에 누적해서 담는다.
for i in range(1,11):
    sum += i
# 4. 누적값을 출력한다.
print(sum)

print("------------------------------")
# 1~100까지의 누적 값

sum = 0
for i in range(1,101):
    sum += i

print(sum)

print("------------------------------")
# 1~5000까지의 누적 합
sum = 0
for i in range(1,5001):
    sum += i
print(sum)

print("------------------------------")
############################################
# 입력받은 구구단 출력
# 몇단? 3

# 3 * 1 = 3 ...

dan = int(input("몇 단?"))
for i in range(1,10):
    print(dan, "*", i, "=", dan*i)