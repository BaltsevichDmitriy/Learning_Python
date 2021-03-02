from random import randint
import turtle

window = turtle.Screen()


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
    frame.goto(width, height)


window.tracer(4)
width = 300
height = 300
number_of_turtles = 33
steps_of_time_number = 600
draw_frame(width, height)

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:  # создание толпы черепашек
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-width, height), randint(-width, height))
    unit.left(randint(3, 270))

for i in range(steps_of_time_number):
    for unit in pool:
        if unit.xcor() > width or unit.xcor() < -width:
            unit.backward(4)
            unit.left(unit.heading() - 180)
        if unit.ycor() > height or unit.ycor() < -height:
            unit.backward(4)
            unit.left(unit.heading() - 180)
        unit.forward(2)
