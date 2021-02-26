import turtle as t
import math


def spyder(peak=12):
    """the turtle draws a snowflake with N peaks"""
    t.shape('turtle')
    t.color('blue', 'orange')
    t.speed(3)
    angle = 0
    radius = 300
    while angle < 360:
        x = radius * math.cos(math.radians(angle))  # зависимость координат от угла и радиуса
        y = radius * math.sin(math.radians(angle))
        t.goto(x, y)
        t.stamp()
        t.goto(0, 0)
        angle += 360 / peak
        t.left(360 / peak)
    t.done()


spyder(22)
