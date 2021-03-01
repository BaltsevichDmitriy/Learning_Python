import turtle as t

t.shape('turtle')
t.width(3)
t.speed(1)
t.color('blue', 'orange')


def go_tur(x, y):
    """move turtle"""
    t.penup()
    t.goto(x, y)
    t.pendown()


def write_num(start_x, number, size):
    """"The Turtle draws the numbers in a font like an index on an envelope"""
    go_tur(start_x, 0)
    if number == 0:
        t.goto(start_x, size)
        t.goto(start_x + (size / 2), size)
        t.goto(start_x + (size / 2), 0)
        t.goto(start_x, 0)
    if number == 1:
        go_tur(start_x, (size / 2))
        t.goto(start_x + (size / 2), size)
        t.goto(start_x + (size / 2), 0)
    if number == 2:
        go_tur(start_x + size / 2, 0)
        t.goto(start_x, 0)
        t.goto(start_x + (size / 2), size / 2)
        t.goto(start_x + (size / 2), size)
        t.goto(start_x, size)
        t.goto(start_x, (size / 2))
    if number == 3:
        t.goto(start_x + (size / 2), size / 2)
        t.goto(start_x, size / 2)
        t.goto(start_x + (size / 2), size)
        t.goto(start_x, size)
    if number == 4:
        go_tur(start_x + size / 2, 0)
        t.goto(start_x + size / 2, size)
        t.goto(start_x + size / 2, size / 2)
        t.goto(start_x, size / 2)
        t.goto(start_x, size)
    if number == 5:
        t.goto(start_x + size / 2, 0)
        t.goto(start_x + size / 2, size / 2)
        t.goto(start_x, size / 2)
        t.goto(start_x, size)
        t.goto(start_x + size / 2, size)
    if number == 6:
        go_tur(start_x, size / 2)
        t.goto(start_x + size / 2, size / 2)
        t.goto(start_x + size / 2, 0)
        t.goto(start_x, 0)
        t.goto(start_x, size / 2)
        t.goto(start_x + size / 2, size)
    if number == 7:
        t.goto(start_x, size / 2)
        t.goto(start_x + size / 2, size)
        t.goto(start_x, size)
    if number == 8:
        go_tur(start_x, size / 2)
        t.goto(start_x + size / 2, size / 2)
        t.goto(start_x + size / 2, 0)
        t.goto(start_x, 0)
        t.goto(start_x, size / 2)
        t.goto(start_x, size)
        t.goto(start_x + size / 2, size)
        t.goto(start_x + size / 2, 0)
    if number == 9:
        go_tur(start_x + size / 2, size / 2)
        t.goto(start_x + size / 2, size / 2)
        t.goto(start_x, size / 2)
        t.goto(start_x, size)
        t.goto(start_x + size / 2, size)
        t.goto(start_x + size / 2, size / 2)
        t.goto(start_x, 0)


start_x = -400
size = 80
A = [9, 4, 1, 7, 0, 0, 6, 7, 8, 9, ]
for i in range(len(A)):
    start_x += (size - (size / 4))
    write_num(start_x, int(A[i]), size)

t.done()
