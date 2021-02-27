import turtle as t
import math


def go_tur(a, b):
    """move turtle"""
    t.penup()
    t.goto(a, b)
    t.pendown()


def stars(star=7):
    """the turtle draws N stars with N rays, times increasing the number of rays of the star by 2"""
    color = 'blue'
    t.color(color, 'orange')
    t.speed(3)
    width = 2
    n_pic = 3
    radius = 100  # радиус звезды
    a = -860
    go_tur(a, 0)
    for i in range(star):  # количество звезд
        if color == 'blue':
            color = 'red'
        elif color == 'red':
            color = 'yellow'
        else:
            color = 'blue'
        t.color(color, 'orange')
        a += 210
        angle = 0
        t.width(width)
        width += 0.5
        n_pic += 2  # колличество лучей
        x = radius * math.cos(math.radians(angle))  # зависимость координат от угла и радиуса
        x = x + a
        y = radius * math.sin(math.radians(angle))
        go_tur(x, y)
        while angle <= 361:
            x = radius * math.cos(math.radians(angle * (n_pic // 2)))  # зависимость координат от угла и радиуса
            x = x + a
            y = radius * math.sin(math.radians(angle * (n_pic // 2)))
            t.goto(x, y)
            angle += (360 / n_pic)
    t.done()


stars()
