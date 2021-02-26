import turtle as t


def square():
    """the turtle draws a square """
    t.width(3)
    t.color("blue", "orange")
    t.begin_fill()
    t.shape('turtle')
    for i in range(4):
        t.forward(250)
        t.left(90)
    t.end_fill()
    t.done()


square()
