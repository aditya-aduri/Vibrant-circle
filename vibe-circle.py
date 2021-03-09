import turtle

time = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("red")

time.pencolor("black")
var_a = 0
var_b = 0
time.speed(0)
time.penup()
time.goto(0,125)
time.pendown()

while True:
    time.forward(var_a)
    time.right(var_b)
    var_a += 2
    var_b += 1

    if var_b == 2000:
        break
    time.hideturtle()

turtle.done()