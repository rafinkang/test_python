# https://programmers.co.kr/learn/courses/30/lessons/12921
# 소수찾기

def solution(n):
    nlist = set([i for i in range(3, n+1, 2)])
    for i in range(3,n+1,2):
        if i in nlist:
            nlist -= set([i for i in range(i*2, n+1, i)])
    
    return len(nlist)+1

print(solution(10))