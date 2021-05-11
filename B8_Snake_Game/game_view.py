from turtle import Turtle
COORDINATE = 375


class Box(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.pu()
        self.goto(-COORDINATE, COORDINATE)
        self.pd()
        for _ in range(4):
            self.forward(COORDINATE * 2)
            self.right(90)
