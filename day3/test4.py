# tupel : list와 유사하지만, 읽기전용

t ='a','b','c','d'
print(t, type(t))

t2 = ('a','b','c','d')
#len 요소의 개수, count a요소의 개수, b의 index벊소
print(t2, type(t2), len(t2), t.count('a'), t.index('b')) 

x = ( 1, 2, 3 )
# x[0] = 10  튜플은 수정불가
print(x)

# ()로는 튜플로 인식 X - ( ,)까지 넣어줘야 튜플로 인식함
x2 = (3)
x3 = (3,)
print(x2, type(x2))
print(x3, type(x3))

# 3을 30으로 수정 -> list로 형변환 한 뒤 수정 -> list를 다시 튜플로
y = list(x)
y[2] = 30
print(y)
x = tuple(y)
print(x)

print("==============================================")
t1 = (10, 20)
# ????????????
#결과 (20,10)
# l1 = list(t1)
# l1[0], l1[1] = l1[1], l1[0]
# print(l1)
# t1 = tuple(l1)
a, b = t1
a, b = b, a
t1 = (a, b)

print(t1) 