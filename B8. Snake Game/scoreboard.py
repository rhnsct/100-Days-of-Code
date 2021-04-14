from turtle import Turtle

FONT_SCORE = ('Arial', 15, 'bold')
FONT_GAME_OVER = ('Arial', 20, 'bold')
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.pu()
        self.sety(375)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT_SCORE)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.sety(0)
        self.write("Game Over.", align=ALIGNMENT, font=FONT_GAME_OVER)
