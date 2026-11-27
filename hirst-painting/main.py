# ###This code will not work in repl.it as there is no access to the colorgram package here.###
# ##We talk about this in the video tutorials##
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# # for color in colors:
# #     rgb_colors.append(color.rgb)
# #
# # print(rgb_colors)
#
# # correct format
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

from random import choice
import turtle as t

# t is turtle module and Turtle(), Screen() are classes in it


DOT_SIZE = 20
GAP = 50
ROWS = 10
COLS = 10

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]
tim = t.Turtle()
screen = t.Screen()
screen.bgcolor("black")
tim.speed("fastest")
# Make turtle invisible
tim.hideturtle()

# changing colormode
t.colormode(255)

# Move turtle to bottom-left corner + little offset(+20)
tim.penup()

width = screen.window_width()
height = screen.window_height()
start_x = -width / 2 + 20
start_y = -height / 2 + 20
tim.goto(start_x, start_y)

current_y = start_y

for _ in range(ROWS):

    for _ in range(COLS):
        color = choice(color_list)

        # r = color[0]
        # g = color[1]
        # b = color[2]
        # dot bina pendown kie bn sakta hai

        tim.dot(DOT_SIZE, color)
        tim.forward(GAP)
        # tim.pendown()
    tim.penup()

    # Move to next row(updating current_y each time)
    current_y = current_y + GAP
    tim.goto(start_x, current_y)

    # or
    # tim.goto(start_x, tim.ycor()+GAP)   ##more simple

screen.exitonclick()
