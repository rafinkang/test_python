import turtle as t

gak = int(input("몇각형 그릴래? :: "))
angle = 0
if gak != 0:
    angle = 360 / gak

t1 = t.Pen()
t1.shape("turtle")
t1.penup()
t1.goto(-100, 100)
t1.pendown()

if angle == 0:
    t1.circle(100)
else:
    for i in range(gak):
        t1.forward(100)
        t1.right(angle)

t.mainloop()