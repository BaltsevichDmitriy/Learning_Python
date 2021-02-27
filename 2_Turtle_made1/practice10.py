import turtle as t


def flower(petals=5):
    """the turtle draws a flower with N pairs of petals"""
    t.color('blue', 'orange')
    t.shape('turtle')
    t.width(3)
    t.speed(9)
    radius = 140
    return_pen = 0
    for i in range(petals):
        t.right(return_pen)
        t.circle(radius)
        t.circle(-1 * radius)
        return_pen = 180 / petals
    t.done()

flower(3)
