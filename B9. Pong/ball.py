from turtle import Turtle


BALL_SIZE = 0.5


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(BALL_SIZE, BALL_SIZE)
        self.color('white')
        self.penup()
        self.x_move = 5
        self.y_move = 5
        self.bounces = 0

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        if 395 > self.xcor() > -395:
            self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1.1
        self.bounces += 1

    def reset_ball(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.x_move = self.x_move / (1.1 ** self.bounces)
        print(self.x_move)
        self.bounces = 0
