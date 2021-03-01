import random as rn
import turtle as t


def brow_move(width=600, height=600):
    """The turtle draws the Brownian motion of molecules"""
    t.width(2)
    t.shape('turtle')
    t.color('red', 'orange')
    for i in range(400):
        t.left(rn.randint(0, 220))
        t.forward(rn.randint(1, 70))
        xy = t.pos()
        if xy[0] >= width / 2:
            t.goto(width / 2 - 10, xy[1])
        if xy[0] <= (-1)*width / 2:
            t.goto(xy[0] + 10, xy[1])
        if xy[1] >= height / 2:
            t.goto(xy[0], height / 2 - 10)
        if xy[1] <= (-1)*height / 2:
            t.goto(xy[0], xy[1] + 10)


brow_move()
