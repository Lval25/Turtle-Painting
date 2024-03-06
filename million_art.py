###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle as turt_mod
import random


turt = turt_mod.Turtle()
turt_mod.colormode(255)
num_of_dots = 100
turt.speed("fastest")
turt.penup()
turt.hideturtle()

#Retrieve colors
"""rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    #rgb_colors.append(color.rgb)
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
"""
color_list = [(246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), 
(138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), 
(101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), 
(168, 99, 102)]



turt.setheading(255)
turt.forward(200)
turt.setheading(0)



# Set dot width and color(random)
for dot in range(1, num_of_dots + 1):
    #set dot size and color
    turt.dot("20", random.choice(color_list))
    turt.forward(50)

    #For every 10 dots got to the next line and continue drawing until finished
    if dot % 10 == 0:
        turt.setheading(90)
        turt.forward(50)
        turt.setheading(180)
        turt.forward(500)
        turt.setheading(0)





screen = turt_mod.Screen()
screen.exitonclick()