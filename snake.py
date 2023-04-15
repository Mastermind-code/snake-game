from turtle import Turtle


class Snake:
    def __init__(self):
        self.segments = []
        self.directions = [(0, 0), (-20, 0), (-40, 0)]
        self.create_snake()
        pass

    def create_snake(self):
        for i in self.directions:
            snake = Turtle('square')
            snake.color('white')
            snake.penup()
            snake.goto(i)
            self.segments.append(snake)

    def move(self, distance):
        for turtle in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[turtle - 1].xcor()
            new_y = self.segments[turtle - 1].ycor()
            self.segments[turtle].goto(new_x, new_y)
        self.segments[0].forward(20)






