import sys

from turtle import Turtle, Screen

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

options = {
    1: "graph u-v",
    2: "graph u-w",
    3: "graph v-w",
    4: "exit"
}

print("Lorenz attractor simulator")
print("==========================")
print("Select option:\n")
for key,val in options.items():
    print("\t", key, " = ", val)
print("")

opt = 0
while opt < 1 or opt > 4:
    opt = int(input("option [1-4]: "))
    if opt < 1 or opt > 4:
        print("Invalid option")

if opt == 4:
    print("bye")
    sys.exit(0)

print("Selected option: ", options.get(opt, "Invalid option"))

#Init turtle
screen = Screen()
screen.setworldcoordinates(-400, -400, 400, 400)

turtle = Turtle()
turtle.speed('fastest')
turtle.penup();

#Draw axis
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

#Draw axis
turtle.pencolor('black')
turtle.penup()
turtle.goto(round(u * 100), round(v * 100));
turtle.pendown()

#Drawing Parameters
fast = 5
p = 0

#Draw graph
for j in range(N):
    for i in range(M):
        us = u + h*s*(v - u)
        vs = v + h*(r*u - v - 20.0*u*w)
        ws = w + h*(5.0*u*v - b*w)

        u = us
        v = vs
        w = ws

        p = p + 1
        if p % fast != 0:
            continue;

        if opt == 1:
            turtle.goto(round(u * 100), round(v * 100))
        elif opt == 2:
            turtle.goto(round(v * 100), round(w * 100))
        elif opt == 3:
            turtle.goto(round(u * 100), round(w * 100))
        
#Wait click to exit
screen.exitonclick()
