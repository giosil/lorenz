import sys

from turtle import Turtle, Screen

options = {
    1: "graph u-v",
    2: "graph u-w",
    3: "graph v-w",
    4: "exit"
}

def getOption():
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
    
    return opt

# Begin
opt = getOption()
if opt == 4:
    print("bye")
    sys.exit(0)

print("Selected option: ", options.get(opt, "Invalid option"))

max = 4

# Init turtle
screen = Screen()
screen.setworldcoordinates(-max * 100, -max * 100, max * 100, max * 100)

turtle = Turtle()
turtle.speed('fastest')
turtle.penup();

# Draw axis
turtle.pencolor('#dddddd')
turtle.penup()
turtle.goto(-max * 100, 0)
turtle.pendown()
turtle.forward(max * 2 * 100)

turtle.penup()
turtle.goto(0, max * 100)
turtle.right(90)
turtle.pendown()
turtle.forward(max * 2 * 100)

# Draw graph title
turtle.penup()
turtle.goto(-max * 100 + 8, max * 100 - 10)
turtle.pendown()
turtle.write(options.get(opt, ""))

# Parameters
M = 1
N = 30000
u0 = 0.82
v0 = 0.63
w0 = 0.74

s = 16.0
r = 46.5
b = 4.0
h = 0.001

fast = 5
p = 0

# Draw start values
u = u0
v = v0
w = w0
turtle.pencolor('black')
turtle.penup()
if opt == 1:
    turtle.goto(round(u * 100), round(v * 100))
elif opt == 2:
    turtle.goto(round(v * 100), round(w * 100))
elif opt == 3:
    turtle.goto(round(u * 100), round(w * 100))
turtle.pendown()

# Draw graph
us = 0
vs = 0
ws = 0
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
        
# Wait click to exit
screen.exitonclick()
