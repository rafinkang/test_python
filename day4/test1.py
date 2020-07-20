# ...
#     set : 순서X, 중복X
# ...

a = {1, 2, 3, 1}

print(a, type(a))

# print(a[0])

b = {3, 4}

print(a.union(b)) #합집합
print(a.intersection(b)) #교집합

print(a-b, a|b, a&b) #차, 합, 교 집합

# b = {3, 4}

# 값 삽입

b.add(5)
print(b)

b.update({6,7})
print(b)

b.update((8,9))
print(b)

b.update([10, 11])
print(b)

# 값 제거

b.discard(7)
print(b)

b.remove(8)
print(b)

print('---------------------------------')


c = set()
c = b
print(c)
c.clear()
print(c)


# 다음 리스트의 중복된 값을 제거하려고 한다.

m = [ 2, 3, 11, 29, 3, 2, 7, 8, 11]

# 리스트 순서O , 중복 O
# 1. set으로 형변환? 중복된 값이 사라진다.
m = set(m)
print(m, type(m))
# 2. 리스트로 변경
m = list(m)
print(m, type(m))
# 3. 정렬 ??
m.sort()
print(m, type(m))