from turtle import Turtle, Screen
import time

# turtle = Turtle()
# turtle.shape('square')
# turtle.color('white')
# turtle = Turtle()
# turtle.shape('square')
# turtle.color('white')
# turtle.goto(x=-20, y = 0)
#
# turtle = Turtle()
# turtle.shape('square')
# turtle.color('white')
# turtle.goto(x=-40, y = 0)
#
screen = Screen()
screen.setup(width=600, height=600)
screen.title('Snake Game')
screen.bgcolor('Black')
screen.tracer(0)
directions = [(0, 0), (-20, 0), (-40, 0)]
turtles = []
for i in directions:
    turtle = Turtle('square')
    turtle.color('white')
    turtle.penup()
    turtle.goto(i)
    turtles.append(turtle)

is_on = True
while is_on:
    time.sleep(1)
    screen.update()

    for turtle in range(len(turtles) - 1, 0, -1):
        new_x = turtles[turtle - 1].xcor()
        new_y = turtles[turtle - 1].ycor()
        turtles[turtle].goto(new_x, new_y)
    turtles[0].forward(40)
    turtles[0].right(90)


screen.exitonclick()


class Snake:
    def __init__(self):
        