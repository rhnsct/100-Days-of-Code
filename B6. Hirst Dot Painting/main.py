# import colorgram
import turtle as t
import random

color_list = [(236, 241, 246), (247, 241, 244), (133, 164, 202), (226, 150, 100),
              (30, 43, 63), (200, 136, 148), (164, 58, 48), (236, 212, 88), (43, 101, 147), (136, 182, 161),
              (148, 63, 71), (159, 33, 30), (58, 47, 44), (51, 41, 45), (169, 29, 33), (60, 116, 99), (215, 83, 74),
              (230, 163, 168), (237, 166, 156), (36, 61, 55), (16, 95, 70), (34, 60, 106), (170, 188, 221),
              (192, 100, 108), (104, 127, 161), (19, 84, 104), (174, 200, 189), (36, 150, 208)]

# num_colors = 30
# colors = colorgram.extract('image.jpg', num_colors)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     color_list.append(rgb)


def make_dots(dots_space, dot_size):
    random_color = random.choice(color_list)
    tom.pd()
    tom.dot(dot_size, random_color)
    tom.pu()
    tom.forward(dots_space)


space_between_dots = 40

tom = t.Turtle()
tom.speed(0)
screen = t.Screen()
screen.colormode(255)
num_dots = int(screen.numinput("Number of dots", "How many dots per row would you like? ", minval=1))
rows = int(screen.numinput("Number of rows", "How many rows would you like?", minval=1))


y = -360
count = 0

while count != rows:
    tom.pu()
    tom.setx(-360)
    tom.sety(y)
    for dots in range(num_dots):
        make_dots(space_between_dots, 15)
    y += space_between_dots
    count += 1


tom.ht()
screen.exitonclick()
