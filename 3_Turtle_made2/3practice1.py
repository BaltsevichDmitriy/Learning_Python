import random as rn
import turtle as t


def brow_move(width=200, height=200):
    """The turtle draws the Brownian motion of molecules"""
    t.width(2)
    t.shape('turtle')
    t.color('red', 'orange')
    for i in range(400):
        t.left(rn.randint(0, 220))
        t.forward(rn.randint(1, 70))
        x = t.xcor()
        y = t.ycor()

        if x >= width:
            t.goto(width - 10, y)
        if x <= -width:
            t.goto(x + 10, y)
        if y >= height:
            t.goto(x, height - 10)
        if y <= - height:
            t.goto(x, y + 10)


brow_move()
