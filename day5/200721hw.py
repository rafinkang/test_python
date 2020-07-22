# 1.
# 	두개 주사위를 던졌을때 합이 4가 되는 모든 경우의수를 출력하는 프로그램을 작성하시요. 
# 	(1,3)
# 	(2,2)
# 	(3,1)

for i in range(1, 7):
    for j in range(1, 7):
        if i+j == 4:
            print("(",i,"+",j,")")
print('--------------------------------------------------')
# 2.
# 특정 연도가 윤년인지 출력하는 프로그램을 작성하시오.
# 	(단 윤년은 4 년마다 한번씩 돌아오며 , 100 년단위로 윤년이 아니며 , 400 년단위로 윤년임)
# 	(EX) 1600 년은 윤년 1900 년은 윤년이 아님 )

# 	출력예
# 	연도입력: 2008
# 	2008 년은 윤년입니다.

year = int(input("연도입력 : "))
if year%400 == 0 or (year%4 == 0 and year%100 != 0):
    print(year, "년은 윤년입니다.")
else:
    print(year, "년은 윤년이 아닙니다.")

print('--------------------------------------------------')

# 3.
# 	print(hap(100,200))
# 	print(minus(200,100)
# 	print(multi(200,3))
# 	print(div(200,3))

def hap(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1 - num2

def multi(num1, num2):
    return num1*num2

def div(num1, num2):
    return num1/num2

print(hap(100,200))
print(minus(200,100))
print(multi(200,3))
print(div(200,3))

print('--------------------------------------------------')

# 4. 
# 	두행렬에 대한 덧셈을 구하세요 
# 	(리스트 사용) 

# 	3, 2, 3			1, 8, 7 
# 	4, 5, 6			6, 4, 4
# 	1, 4, 9			3, 2, 3
# 반복문을 사용해서 값을 할당하고 화면에 출력하세요 

# 		4, 10, 10
# 		10, 9, 10
# 		4,  6, 12 

list1 = [
    [3, 2, 3],
    [4, 5, 6],
    [1, 4, 9]
]

list2 = [
    [1, 8, 7],
    [6, 4, 4],
    [3, 2, 3]
]

list3 = []

for i in range(3):
    list3.append([])
    for j in range(3):
        list3[i].append(int(list1[i][j]) + int(list2[i][j]))

print(list3)



print('--------------------------------------------------')
# 5.
# 	5행 5열자리 리스트를  만들고

# 	1  2  3  4  5
# 	6  7  8  9 10
# 	11 12 13 14 15
# 	16 17 18 19 20
# 	21 22 23 24 25
list4 = []

for i in range(5):
    list4.append([])
    for j in range(5):
        list4[i].append((j+1)+(i*5))

print(list4)
print('--------------------------------------------------')

# 6.
# 	사용자로부터 10명의 성적 데이터를 입력받아  배열에 담고
# 	학생들의 총점과 평균을 화면에 출력하세요 

list5 = []

for i in range(10):
    list5.append(int(input("성적을 입력하세요. : ")))

total = sum(list5)
avg = total / len(list5)

print("총점 :", total, "평균 :", avg)

print('--------------------------------------------------')
# 7. 
# 	길이가 100개인 정수형 리스트에 정수 1~100의 값을 대입

list6 = []
for i in range(1, 101):
    list6.append(i)

print(list6)

print('--------------------------------------------------')
# 8. 
# 	7번 에서 3의 배수는 3333  5의 배수는 5555
# 	3과5의 공배수는 3535 를 대입하세요 

list7 = []
for i in list6:
    if i%3 == 0 and i%5 == 0:
        list7.append(3535)
    elif i%3 == 0:
        list7.append(3333)
    elif i%5 == 0:
        list7.append(5555)
    else:
        list7.append(i)

print(list7)

print('--------------------------------------------------')
# 9.
# 	정수 10개를 입력받아 리스트에 저장하고, 리스트에 있는 정수 중에서 3의 배수만 출력해보자.


list8 = []
for i in range(10):
    list8.append(int(input("정수를 입력하세요. : ")))

for i in list8:
    if i%3 == 0:
        print(i);