import turtle

class snake:
    def __init__(self):
        self.name = 'hello world'
        directions = [(0, 0), (-20, 0), (-40, 0)]
        for i in directions:
            turtle = Turtle('square')
            turtle.color('white')
            turtle.penup()
            turtle.goto(i)
            turtle.append(turtle)


