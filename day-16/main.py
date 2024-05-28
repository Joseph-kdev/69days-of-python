# from turtle import Turtle, Screen

# joey = Turtle()
# joey.shape('turtle')
# joey.color("cyan", "green")
# joey.forward(100)

# my_screen = Screen()
# my_screen.exitonclick()

##Install prettytable
from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon name", ["Pikachu", "Squirtle"])
table.add_column("type", ["electric", "water"])


