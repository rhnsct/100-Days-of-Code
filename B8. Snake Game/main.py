from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from game_view import Box
import time

screen = Screen()
screen.setup(width=810, height=810)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
game_limits = Box()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
game_is_on = True

while game_is_on:
    snake.move()
    screen.update()

    if snake.head.distance(food) < 9:
        food.refresh()

        snake.extend()

        scoreboard.increase_score()

    if snake.head.xcor() > 368 or snake.head.xcor() < -368 or snake.head.ycor() > 368 or snake.head.ycor() < -368:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.snake_parts[1:]:

        if snake.head.distance(segment) < 5:
            game_is_on = False
            scoreboard.game_over()
    time.sleep(0.07)

screen.exitonclick()
