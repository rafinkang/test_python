# import turtle as t
from turtle import *

name = textinput("이름", "당신의 이름을 입력하세요.")
print(name)
shape('turtle')
color('#ff6600')

lt(90)

# 몇개의 명령들을 모아서 이름을 부여해 놓은것 : 함수
# 자주 사용하는 기능
def w():
    fd(50)

def d():
    rt(90)
    fd(50)

def a():
    lt(90)
    fd(50)

def s():
    lt(180)
    fd(50)


# 함수와 키 연결
onkey(w, "w") 
onkey(d, "d") 
onkey(a, "a") 
onkey(s, "s") 

listen()


mainloop()