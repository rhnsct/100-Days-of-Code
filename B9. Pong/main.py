from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

RIGHT_SIDE = (350, 0)
LEFT_SIDE = (-350, 0)

screen = Screen()
screen.screensize(canvwidth=800, canvheight=800)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(RIGHT_SIDE)
left_paddle = Paddle(LEFT_SIDE)
ball = Ball()
score = Score()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_on = True


while game_on:

    screen.update()
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if ball.distance(right_paddle) < 51 and ball.xcor() > 330 or ball.distance(left_paddle) < 51 and ball.xcor() < -330:
        ball.bounce_x()

    if ball.xcor() > 345:
        score.l_score += 1
        score.keep_score()
        ball.reset_ball()
        right_paddle.goto(RIGHT_SIDE)
        left_paddle.goto(LEFT_SIDE)

    if ball.xcor() < -345:
        score.r_score += 1
        score.keep_score()
        ball.reset_ball()
        right_paddle.goto(RIGHT_SIDE)
        left_paddle.goto(LEFT_SIDE)

    time.sleep(0.015)

screen.exitonclick()
