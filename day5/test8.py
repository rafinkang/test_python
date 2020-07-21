
m = [3, 0, 1, 8 ,7, 2, 5, 4, 6, 9]
copy = m.copy()
print(m)

# 버블정렬
print(len(m))

for j in range(len(m)-1, 0 , -1):
    for i in range(j):
        if m[i] > m[i+1]:
            m[i], m[i+1] = m[i+1], m[i]

print('-------------------------')
print(m)

# 정렬 함수
print(sorted(copy))
copy.sort()
print(copy)


