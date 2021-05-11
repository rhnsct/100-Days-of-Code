from turtle import Turtle

FONT_SCORE = ('Arial', 15, 'bold')
FONT_GAME_OVER = ('Arial', 20, 'bold')
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.pu()
        self.goto(0, 375)
        self.hideturtle()
        self.color('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT_SCORE)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()
