# map : built-in : list 나 dictionary와 같은 iterable한 데이터를 인자로 받아
# list 안에 개별 item을 함수의 인자로 전달하여 결과를 list형태로 주는 함수

def func1(x):
    return x*2

m = [10, 20, 30, 40]
n = []
for i in range(len(m)):
    n.append(func1(m[i]))
print(n) # [20,40,60,80]

print(list(map(func1, m)))

t = { 1:100, 2:200, 3:300}
print(list(map(func1, t))) #key값이 func1에 들어감
print(list(map(func1, [ t[i] for i in t ]))) # key값을 찾아서 매핑시킴

print('--------------------------')
a = [1,2,3,4,5,6,7,8,9,10]

# 3의 배수만 출력
print([str(i) for i in a if i%3==0])

# makeString(x)
# 'x'
def makeString(x):
    if x%3 == 0:
        return str(x)
    else:
        return x

# print(list(map(makeString, [i for i in a if i%3==0])))
print(list(map(makeString, a)))

print(list(map((lambda a: str(a) if a%3==0 else a), a)))


# 소수
# 소수면 실수로 리턴 : float
# 아니면 자기 자신 리턴
def primeNumber(x):
    for i in range(2, x):
        if x%i == 0:
            return x
    return float(x)

print(primeNumber(4))
print((lambda a1: float(a1) if len([a1 for i in range(2, a1) if a1%i ==0]) == 0 else a1)(8))
print('--------------------------------------------')

def test2(x):
    if x>0 : 
        return x
    else:
        return None

n = [-3,-2,-1,0,1,2,3]

print(list(filter(test2, n)))
print(list(filter(lambda x : x>0, n)))

#60이하는 탈락
score = [80, 70, 53, 90, 70, 80, 49, 99]
print(list(filter(lambda s : s > 60, score)))

# 70 ~ 90
print(list(filter(lambda s : s > 70 and s < 90, score)))
print('--------------------------------------------')

# 현재 작업디렉토리에서 파일들의 목록 가져와

file_names = ['movie1.jpg', 'movie2.png', 'rabbit.png', 'bg.png', 'test.txt', 'test2.py']

# *png 파일의 확장자만 검사해서 파일의 이름
# 'asdf'.find('a')


def png_finder(x):
    if x.find(".png") != -1:
        return x
    else:
        return None

# print(list(filter(함수, Arr)))
print(png_finder("movie.png"))
print(list(filter(png_finder, file_names)))
print(list(filter(lambda f_name: f_name.find('.png') > 0, file_names))) 
print(list(filter(lambda f_name: f_name.find('.png') != -1, file_names))) 
