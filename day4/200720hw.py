import turtle as t

t1 = t.Pen()
t1.speed(0)
# t1.shape("turtle")
t1.circle(200)

t1.penup()
t1.goto(-70, 250)
t1.pendown()
t1.circle(40)

t1.penup()
t1.goto(70, 250)
t1.pendown()
t1.circle(40)

t1.penup()
t1.goto(-70, 270)
t1.pendown()
t1.begin_fill()
t1.fillcolor("black")
t1.circle(20)
t1.end_fill()

t1.penup()
t1.goto(70, 270)
t1.pendown()
t1.begin_fill()
t1.fillcolor("black")
t1.circle(20)
t1.end_fill()

# 왼니
t1.penup()
t1.goto(-60, 100)
t1.pendown()
t1.begin_fill()
t1.fillcolor("black")
for i in range(4):
    t1.fd(50)
    t1.rt(90)
t1.end_fill()

# 오른니
t1.penup()
t1.goto(10, 100)
t1.pendown()
for i in range(4):
    t1.fd(50)
    t1.rt(90)

# 입
t1.penup()
t1.goto(-100, 180)
t1.pendown()
t1.begin_fill()
t1.fillcolor("white")
t1.right(90)
t1.circle(100, 180)
t1.end_fill()


t.mainloop()