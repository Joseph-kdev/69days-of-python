from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape('turtle')

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

colors = ['red', 'cyan', 'pink', 'orange', 'brown', 'yellow', 'green', 'DarkOrchid', 'IndianRed', 'wheat']

# for n in range(3, 11):
#     tim.color(random.choice(colors))
#     for _ in range(n):
#         tim.forward(100)
#         tim.left(360/n)


# for _ in range(100):
#     tim.color(random.choice(colors))
#     tim.pensize(5)
#     tim.forward(random.randint(0, 100))
#     tim.left(random.randrange(0, 360))

# directions = [0 , 90, 180, 270]
# tim.speed('fastest')

# for _ in range(300):
#     tim.color(random.choice(colors))
#     tim.pensize(5)
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

tim.speed('fastest')
tim.pensize(3)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random.choice(colors))
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
    
draw_spirograph(5)

screen = Screen()
screen.exitonclick()