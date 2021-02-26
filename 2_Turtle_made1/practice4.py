import turtle as t


def circle():
    """ the turtle draws a circle """
    t.width(3)
    t.color("green", "orange")
    t.begin_fill()
    t.shape('turtle')
    for i in range(360):
        t.forward(2)
        t.left(1)
    t.end_fill()
    t.done()


circle()
