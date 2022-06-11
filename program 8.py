# program to draw a red color thick pen on a yellow background.
import turtle
turtle.bgcolor("yellow")
turtle.color("red")
turtle.pensize(10)
for angle in range(0, 360, 30):
    turtle.seth(angle)
    turtle.circle(100)