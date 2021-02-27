import turtle as t


def go_tur(a, b):
    """move turtle"""
    t.penup()
    t.goto(a, b)
    t.pendown()


def smile():
    """the turtle draws a smile"""
    go_tur(0, -170)
    t.color('blue', 'yellow')
    t.begin_fill()
    t.circle(200)
    t.end_fill()
    t.color('blue', 'blue')
    t.begin_fill()
    go_tur(100, 80)
    t.circle(45)
    t.end_fill()
    go_tur(-100, 80)
    t.begin_fill()
    t.circle(45)
    t.end_fill()
    t.width(25)
    t.color('black', 'black')
    go_tur(0, 70)
    t.goto(0, 0)
    t.color('red', 'red')
    go_tur(120, -20)
    t.right(90)
    t.circle(-120, 180)
    t.done()


smile()
