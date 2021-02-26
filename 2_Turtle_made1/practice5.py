import turtle as t


def nested_squares(number_square=10):
    """ the turtle draws N nested squares"""
    t.width(3)
    t.color('blue', 'gray')
    t.shape('turtle')
    coord_value = 17
    start_position = [coord_value, coord_value]
    for i in range(number_square):
        t.penup()
        t.goto(start_position)
        t.pendown()
        t.goto(-1 * coord_value, coord_value)
        t.goto(-1 * coord_value, -1 * coord_value)
        t.goto(coord_value, -1 * coord_value)
        t.goto(coord_value, coord_value)
        coord_value += 18
        start_position = [coord_value, coord_value]
    t.penup()
    t.goto(0, 0)
    t.done()


nested_squares(11)
help(t.color)
