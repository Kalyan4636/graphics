# To draw a random pattern of circle, square, rectangle.
import turtle as t
def square(x):
    for i in range(4):
        t.forward(x)
        t.left(90)
def rectangle(x,y):
    t.forward(x)
    t.left(90)
    t.forward(y)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(y)

def draw_shape(x, y):
    t.penup()
    t.setpos(x, y)
    t.pendown()
    t.begin_fill()
    if x <= 50: # left third.
        t.color("red")
        square(10)
    elif 50 < x <= 150: # middle third.
        t.color("yellow")
        t.circle(10)
    else: # right third.
        t.color("purple")
        rectangle(10, 20)
t.onscreenclick(draw_shape)
t.mainloop()