from turtle import Turtle, Screen

tuts = Turtle()


def move_forward():
    tuts.forward(10)


def move_backward():
    tuts.backward(10)

def turn_left():
    tuts.left(10)
    
def turn_right():
    tuts.right(10)
    

def clear():
    tuts.clear()
    tuts.penup()
    tuts.home()
    tuts.pendown()
    
screen = Screen()


screen.listen()
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=clear)
screen.exitonclick()