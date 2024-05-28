# import colorgram

# colors = colorgram.extract('./hirst.png', 2 ** 32)

# color_pallete = []

# for color in colors:
#     my_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
#     color_pallete.append(my_tuple)
    
# print(color_pallete)

color_list = [(252, 250, 247), (253, 247, 249), (237, 251, 245), (249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 
40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 
97, 62), (5, 38, 33), (68, 219, 155), (238, 157, 212), (86, 77, 208), (86, 225, 235), (250, 8, 14), (242, 166, 157), (177, 180, 224), (36, 243, 159), (6, 81, 115), (11, 55, 248)]

import turtle as turtle_module
import random

turtle_module.colormode(255)
tuts = turtle_module.Turtle()
tuts.speed('fastest')
tuts.penup()
tuts.hideturtle()
tuts.setheading(225)
tuts.forward(300)
tuts.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tuts.dot(20, random.choice(color_list))
    tuts.forward(50)
    
    if dot_count % 10 == 0:
        tuts.setheading(90)
        tuts.forward(50)
        tuts.setheading(180)
        tuts.forward(500)
        tuts.setheading(0)







screen = turtle_module.Screen()
screen.exitonclick()