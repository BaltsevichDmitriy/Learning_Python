import turtle as t


def spring(half_spiral=5):
    """the turtle draws a spring with N spirals"""
    t.color('red', 'blue')
    t.speed(8)
    t.shape('turtle')
    t.width(2)
    t.right(270)
    radius1 = -70
    radius2 = -10
    t.penup()
    t.goto(-340, 0)
    t.pendown()
    extend = 180
    for i in range(half_spiral):
        t.circle(radius1, extend)
        t.circle(radius2, extend)
    t.done()


spring()
