# import colorgram
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
Screen().title('Beautiful Hirst Painting')

# Method to extract colors from an image

# colors = colorgram.extract('hirst_painting.jpg', 35)
# color_palette = []

# for color in colors:
#     color_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
#     color_palette.append(color_tuple)

# print(color_palette)


color_list = [(223, 236, 228), (236, 230, 216), (140, 176, 207), (25, 32, 48), (26, 107, 159), (237, 225, 235),
              (209, 161, 111), (144, 29, 63), (230, 212, 93), (4, 163, 197), (218, 60, 84), (229, 79, 43),
              (195, 130, 169), (54, 168, 114), (28, 61, 116), (172, 53, 95), (108, 182, 90), (110, 99, 87),
              (193, 187, 46), (240, 204, 2), (1, 102, 119), (19, 22, 21), (50, 150, 109), (172, 212, 172),
              (118, 36, 34), (221, 173, 188), (227, 174, 166), (153, 205, 220), (184, 185, 210), (77, 37, 76),
              (120, 117, 155), (35, 35, 35)]

shape_list = ['arrow', 'circle', 'classic', 'square', 'triangle', 'turtle']

my_screen = Screen()
my_screen.setup(500, 500)

# Setting the object in the bottom left corner of the window
my_screen.setworldcoordinates(-40, -40, my_screen.window_width() - 1, my_screen.window_height() - 1)

my_turtle = Turtle()
my_turtle.penup()
my_turtle.speed('fast')

for count in range(10):
    x = my_turtle.xcor()
    y = my_turtle.ycor()
    my_turtle.shape(random.choice(shape_list))
    for _ in range(10):
        random_color = random.choice(color_list)
        my_turtle.pencolor(random_color[0], random_color[1], random_color[2])
        my_turtle.color(random_color[0], random_color[1], random_color[2])
        my_turtle.dot(20)

        my_turtle.forward(50)

    my_turtle.setx(x)
    my_turtle.sety(y + 50)

my_turtle.hideturtle()
my_screen.exitonclick()
