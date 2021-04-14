from turtle import Turtle
STARTING_LOCATIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_parts = []
        self.make_snake()
        self.head = self.snake_parts[0]

    def make_snake(self):
        for position in STARTING_LOCATIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle(shape='square')
        snake.color('white')
        snake.up()
        snake.goto(position)
        snake.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.snake_parts.append(snake)

    def extend(self):
        self.add_segment(self.snake_parts[-1].position())
        self.add_segment(self.snake_parts[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[seg_num - 1].xcor()
            new_y = self.snake_parts[seg_num - 1].ycor()
            self.snake_parts[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
