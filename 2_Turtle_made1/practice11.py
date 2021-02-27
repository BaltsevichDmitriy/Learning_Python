import turtle as t


def butterfly(petals=11):
    """the turtle draws a butterfly with N pairs of petals"""
    t.color('pink', 'orange')
    t.shape('turtle')
    t.width(2)
    t.speed(0)
    radius = 10
    t.right(90)
    for i in range(petals):
        t.circle(radius)
        t.circle(-1 * radius)
        radius += 10
    t.right(180)
    t.done()


butterfly()
