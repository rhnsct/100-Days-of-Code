import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

score = Scoreboard()
car_manager = CarManager()
player = Player()

screen.listen()
screen.onkey(player.move_forward, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    car_manager.make_car()
    car_manager.move_cars()
    score.write_score()
    if player.is_at_finish():
        score.level += 1
        player.go_to_start()
        car_manager.increase_speed()

    for vehicle in car_manager.all_cars:
        x_cor_dif = player.xcor() - vehicle.xcor()
        y_cor_dif = player.ycor() - vehicle.ycor()
        if -29 < x_cor_dif < 29:
            if -19 < y_cor_dif < 19:
                game_is_on = False
                score.game_over()
    screen.update()

screen.exitonclick()
