import turtle as t


def square_spiral(square=5):
    """the turtle draws a square spiral with N squares"""
    t.color('red', 'orange')
    t.shape('turtle')
    t.width(3)
    t.speed(2)
    thick = 11
    line_long = 10
    for i in range(square * 4):
        t.forward(line_long)
        t.right(90)
        line_long += thick
    t.done()


square_spiral(7)
