import turtle
turtle.bgcolor('black')
turtle.speed(0)
turtle.pencolor('blue')
turtle.pensize(2)

turtle.penup()
turtle.goto(-100,-55)
turtle.pendown()

for i in range(100):
    turtle.forward(200)
    turtle.left(115)
turtle.hideturtle()
turtle.done()