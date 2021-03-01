from random import randint
import turtle

window = turtle.Screen()
window.tracer(1)


def draw_frame(width=350, height=350):
    frame = turtle.Turtle()
    frame.hideturtle()
    frame.pensize(3)
    frame.speed(0)
    frame.penup()
    frame.goto(width, height)
    frame.pendown()
    frame.goto(-width, height)
    frame.goto(-width, -height)
    frame.goto(width, -height)
    frame.goto(width, height)


width = 300
height = 300
number_of_turtles = 3
steps_of_time_number = 300
draw_frame(width, height)

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:  # создание толпы черепашек
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-width, height), randint(-width, height))

xy = [[0, 0, 2.3, 3.2]] * number_of_turtles
#x_speed = 1.2
#y_speed = 2.1
for i in range(steps_of_time_number):
    j = 0
    for unit in pool:
        unit.goto(unit.xcor() + xy[j][2], unit.ycor() + xy[j][3])
        if unit.xcor() >= width or unit.xcor() <= -width:
            xy[j][2] = -xy[j][2]
        if unit.ycor() >= height or unit.ycor() <= -height:
            xy[j][3] = -xy[j][3]
        xy[j][0] += 1
        xy[j][1] += 1
        print(unit.xcor(),unit.ycor())
        print(j)
        j += 1
    print(xy)
