from random import randint
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
y_positions = [-125, -75, -25, 25, 75, 125]
all_turtles = []

user_bet = screen.textinput(title="Bet", prompt="What color would you like to bet on?\n(red/blue/green/purple/orange)")

for n in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.pu()
    new_turtle.color(colors[n])
    new_turtle.goto(x=-240, y=y_positions[n])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        random_distance = randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The winning color was {winning_color}.")

            else:
                print(f"You lost. The winning color was {winning_color}.")



screen.exitonclick()
