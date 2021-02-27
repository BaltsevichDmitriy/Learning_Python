import turtle as t
import math


def regular_polygon(polygon=10):
    """the turtle draws N nested regular polygon """
    t.color('gray', 'orange')
    t.speed(5)
    t.width(3)
    t.shape('turtle')
    thick_between = 30
    radius = 30
    pik = 3
    t.left(45)
    for i in range(polygon):
        angle = 0
        t.penup()
        t.goto(radius * math.cos(math.radians(angle)), radius * math.sin(math.radians(angle)))
        t.pendown()
        while angle <= 362:
            x = radius * math.cos(math.radians(angle))  # зависимость координат от угла и радиуса
            y = radius * math.sin(math.radians(angle))
            t.goto(x, y)
            angle += 360 / pik
            t.left(360 / pik)
        t.right(344 / pik)
        pik += 1
        radius += thick_between
    t.penup()
    t.goto(0, 0)
    t.done()


regular_polygon()
