from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# timmy.color("coral")
# timmy.shape("turtle")
# timmy.forward(100)

# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Pokemon name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])
table.align = "l"

print(table)


