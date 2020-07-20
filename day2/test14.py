############################################
# 입력받은 구구단 출력
# 몇단? 3

# 3 * 1 = 3 ...

# dan = int(input("몇 단?"))
# for i in range(1,10):
#     print(dan, "*", i, "=", dan*i)



# 1부터 50사이의 홀수를 리스트로 만들어 화면에 출력
# 반복문으로  출력
m = list(range(1, 50, 2))
for i in m:
    print(i, end=' ');

k = [3, 6, 9, 12, 15, 18]

# enumerate(*args, **kwargs)
# Return an enumerate object.
# iterable an object supporting iteration
# The enumerate object yields pairs containing a count (from start, which defaults to zero) and a value yielded by the iterable argument.
# enumerate is useful for obtaining an indexed list: (0, seq[0]), (1, seq[1]), (2, seq[2]), ...

# k[index]
# (인덱스 번호, 컬렉션의 엘리먼트) ==> tuple 형태로 반환
for i in enumerate(k):
    print(i)


# 리스트
m = [];
m.append(100)
m.append(200)
print(m)
# [100, 200]

# n 리스트에 500, 300의 요소를 추가
n = [];
n.append(500)
n.append(300)
print(n)
# [500, 300]

print(m+n)
# [100, 200, 500, 300]

print(list("닭백숙"))
# ['닭', '백', '숙']

# 880101-1234567
# 88년 01월 01일    1 로 출력

arr1 = list("880101-1234567")
print(arr1[0]+arr1[1]+"년 "+arr1[2]+arr1[3]+"월 "+arr1[4]+arr1[5]+'일 \t'+arr1[7])

s = "천만 탈모인 희소식 들판 야생화에서 발모제 성분 발견".split()
print(s)
# index
print(s[0])
print(s[5])
print(s[-1])

# slice - 리스트 자르는 특별한 문법 ㅡㅡ 
print(s[1:3])
# 리스트명[시작인덱스:종료인덱스:step] 종료인덱스의 원소는 포함되지 않고 바로 앞 요소까지만 포함
print(s[1:5])

# 들판 야생화에서 발모제 
# s 리스트에서 일부를 slice해서 k 리스트를 만들고 

k = []
# k.append(s[3:6])
k += s[3:6]
print(k)

t = "동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세"

# t[시작:종료:step] 미지정시 끝까지 # 전체 지정 = t[:]
#['하느님이', '보우하사', '우리나라', '만세']
t1 = t.split()
# t2 = t1[4:8] 
t2 = t1[4:]
print(t2) 

# 반복을 사용해서 출력
for i in t2:
    print(i, end=" ")

print('--------------------------------------------------------------')
print(t[::2]) #step 2단계씩
print(t[::-1]) #reverse

# a = [1,3,9,8]
a = [3,0,1,8,7,2,5,4,6,9]
print(a) #정렬해서 출력
# 정렬
print(sorted(a))
a.sort()
print(a)
a.reverse()
print(a)


print('--------------------------------------------------------------')
# 1부터 100까지의 값을 요소로 갖는 k리스트를 작성
k = list(range(1,101));
print(k)
print('--------------------------------------------------------------')
# 25~-45번까지 요소를 잘라와 v리스트를 생성
v = k[24:45]
print(v)
print('--------------------------------------------------------------')
# 반복문을 사용해서 홀수 번째 요소만 출력
for i in v[::2]:
    print(i)