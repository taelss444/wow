import turtle
s = turtle.getscreen()
t = turtle.Turtle()
turtle.bgcolor("pink")
turtle.title("Рисовашки")
t.shapesize(3, 3, 3)
t.pen(pencolor="purple", fillcolor="purple", pensize=5, speed=2)
for i in range(4):
    t.fd(100)
    t.rt(90)
n = 10
while n <= 50:
    t.circle(n)
    n = n + 10
u = input("Do you want me to draw a square? ")
if u == "yes":
    for i in range(4):
        t.fd(50)
        t.rt(90)
elif u == "no":
    print("Okay.")
else:
    print("Try again! ")
