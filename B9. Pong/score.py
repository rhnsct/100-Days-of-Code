from turtle import Turtle

ALIGNMENT = 'center'
SCORE_FONT = ('Arial', 20, 'bold')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.pensize(3)
        self.color('white')
        self.speed(0)
        self.hideturtle()
        self.keep_score()

    def draw_net(self):
        self.penup()
        self.goto(0, -280)
        self.pendown()
        self.setheading(90)
        for _ in range(29):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()

    def draw_court(self):
        self.penup()
        self.goto(-400, 300)
        self.pendown()
        self.setheading(0)
        for _ in range(2):
            self.forward(800)
            self.right(90)
            self.forward(600)
            self.right(90)
        self.draw_net()

    def keep_score(self):
        self.clear()
        self.draw_court()
        self.penup()
        self.goto(0, 320)
        self.write(f"{self.l_score} : {self.r_score}", align=ALIGNMENT, font=SCORE_FONT)

