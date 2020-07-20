import turtle as t

# 꼬부기
t.shape("turtle")
# 컬러
t.color("red")
# while True:
#     # 앞으로 100 이동
#     t.forward(100)
#     # 오른쪽으로 90도
#     t.right(145)

# foward = fd, left = lt right = rt
t2 = t.Pen()
t2.shape("turtle")
t2.color('#ff6600')
t2.penup() # 펜 들기 -> 그리지 않는다
t2.goto(-200, 100) # 좌표로 이동
t2.pendown() #펜 내려놓기 -> 그리기
t2.begin_fill() #채우기 시작
t2.fillcolor("#ff6600") #채우기 색
t2.circle(25) #반지름
t2.end_fill() #채우기 끝


t3 = t.Pen()
t3.shape("turtle")
t3.shapesize(3)
t3.color("blue")

t3.penup()
t3.goto(100, 100)
t3.pendown()
for i in range(5):
    t3.fd(100)
    t3.rt(72)
    
t4 = t.Pen()
t4.shape("turtle")
t4.shapesize(2)
t4.penup()
t4.goto(200, 100)
t4.pendown()
# circle(radius, extent=None, steps=None)
t4.circle(20, 100)


while True:
    # 앞으로 100 이동
    t.forward(100)
    # 오른쪽으로 90도
    t.right(145)
# 창 안닫히게 - 계속 반복시키는거
t.mainloop()