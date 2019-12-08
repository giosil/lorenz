from turtle import Turtle, Screen

screen = Screen()
screen.setworldcoordinates(-400, -400, 400, 400)

turtle = Turtle()
turtle.speed('fastest')
turtle.penup();

M = 1
N = 30000
u0 = 0.82
v0 = 0.63
w0 = 0.74

s = 16.0
r = 46.5
b = 4.0
h = 0.001

u = u0
v = v0
w = w0
us = 0
vs = 0
ws = 0

turtle.pencolor('#dddddd')
turtle.penup()
turtle.goto(-400,0)
turtle.pendown()
turtle.forward(800)

turtle.penup()
turtle.goto(0,400)
turtle.right(90)
turtle.pendown()
turtle.forward(800)

turtle.pencolor('black')
turtle.penup()
turtle.goto(round(u * 100), round(v * 100));
turtle.pendown()

fast = 5
count = -1

for j in range(N):
    for i in range(M):
        us = u + h*s*(v - u)
        vs = v + h*(r*u - v - 20.0*u*w)
        ws = w + h*(5.0*u*v - b*w)

        u = us
        v = vs
        w = ws

        count = count + 1
        if count % fast != 0:
            continue;
        
        turtle.goto(round(u * 100), round(v * 100));
        turtle.pendown()

screen.exitonclick()
