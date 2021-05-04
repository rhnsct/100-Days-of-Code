from turtle import Turtle

MOVE_DISTANCE = 25


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.penup()
        self.goto(position)
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color('white')


    def up(self):
        if self.ycor() < 241:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -241:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)



