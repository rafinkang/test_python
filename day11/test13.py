from turtle import *
import random

a = Turtle()
screen = Screen()
print(a)
print(screen)

screen.addshape("audience.gif")
a.shape("audience.gif")
a.penup()
a.goto(0, 225)

t1 = Turtle()
t1.color("red")
t1.shape("turtle")
t1.penup()
t1.goto(-400, 0)
t1.pendown()
t1.write("1번 꼬부기")

t2 = Turtle()
t2.color("blue")
t2.shape("turtle")
t2.penup()
t2.goto(-400, -30)
t2.pendown()
t2.write("2번 꼬부기")

t3 = Turtle()
t3.color("green")
t3.shape("turtle")
t3.penup()
t3.goto(-400, -60)
t3.pendown()
t3.write("3번 꼬부기")

t4 = Turtle()
t4.color("orange")
t4.shape("turtle")
t4.penup()
t4.goto(-400, -90)
t4.pendown()
t4.write("4번 꼬부기")

t5 = Turtle()
t5.color("purple")
t5.shape("turtle")
t5.penup()
t5.goto(-400, -120)
t5.pendown()
t5.write("5번 꼬부기")

t6 = Turtle()
t6.color("black")
t6.shape("turtle")
t6.penup()
t6.goto(-350, 0)
t6.pendown()
for i in range(5):
    t6.right(90)
    t6.fd(120)
    t6.left(90)
    t6.penup()
    t6.fd(100)
    t6.pendown()
    t6.left(90)
    t6.fd(120)
    t6.right(90)
    t6.penup()
    t6.fd(100)
    t6.pendown()
t6.penup()
t6.goto(1000,1000)

n = textinput("골라", "언눔한테 얼마걸래?")
a.color("red")
# a.write(n+"번 꼬부기 이겨라")

dis1 = 0
dis2 = 0
dis3 = 0
dis4 = 0
dis5 = 0
for i in range(250):
    rnd1 = random.randint(1,5)
    dis1 += rnd1
    t1.fd(rnd1)
    rnd2 = random.randint(1,5)
    dis2 += rnd2
    t2.fd(rnd2)
    rnd3 = random.randint(1,5)
    dis3 += rnd3
    t3.fd(rnd3)
    rnd4 = random.randint(1,5)
    dis4 += rnd4
    t4.fd(rnd4)
    rnd5 = random.randint(1,5)
    dis5 += rnd5
    t5.fd(rnd5)
    
    if dis1 >= 735:
        if n == 1 : 
            a.write("배팅성공!")
        else:
            a.write("1번 꼬부기 승리!")
        break
    elif dis2 >= 735:
        if n == 2 : 
            a.write("배팅성공!")
        else:
            a.write("2번 꼬부기 승리!")
        break
    elif dis3 >= 735:
        if n == 3 : 
            a.write("배팅성공!")
        else:
            a.write("3번 꼬부기 승리!")
        break
    elif dis4 >= 735:
        if n == 4 : 
            a.write("배팅성공!")
        else:
            a.write("4번 꼬부기 승리!")
        break
    elif dis5 >= 735:
        if n == 5 : 
            a.write("배팅성공!")
        else:
            a.write("5번 꼬부기 승리!")
        break




















mainloop()