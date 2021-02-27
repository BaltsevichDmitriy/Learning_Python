import turtle as t
import math


def spiral(ring=5):
    """the turtle draws a spiral with N rings"""
    t.color('blue', 'green')
    t.shape('turtle')
    t.width(3)
    t.speed(0)
    radius = 2
    think = 20
    t.left(90)
    delta = 8
    for i in range(ring):
        angle = 0
        for ii in range(int(360/delta)):
            x = radius * math.cos(math.radians(angle))
            y = radius * math.sin(math.radians(angle))
            t.goto(x, y)
            angle += delta
            radius += think / (360/delta)
            t.left(delta)
    t.done()


spiral(10)
