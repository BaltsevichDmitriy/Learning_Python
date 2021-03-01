import turtle

# make the floor
floor = turtle.Turtle()
floor.hideturtle()
floor.pensize(5)
floor.speed(0)
floor.goto(-450, 0)
floor.goto(450, 0)

# make the ball jumping
window = turtle.Screen()
ball = turtle.Turtle(shape='circle')
ball.pensize(3)
ball.color('blue')
ball.speed(0)
ball.penup()
ball.goto(-400, 5)
ball.pendown()
Vy = 5  # скорость по оси y
dt = 0.05  # отрицательное прирощение скорости по оси y
Vx = 1.2  # скорость по оси x
while Vx > 0.01:
    ball.goto(ball.xcor() + Vx, ball.ycor() + Vy)
    Vy -= dt
    if ball.ycor() <= 0:
        Vy = -Vy + Vy * 0.2
        Vx -= 0.14
        ball.goto(ball.xcor(), 0)
ball.speed(1)
ball.goto(ball.xcor() + 9, 13)

window.mainloop()
