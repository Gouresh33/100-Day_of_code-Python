# From Day 16 onwards, you will be creating your own PyCharm projects from scratch.
# Instead of using templates that I have created for you.
# It will be another step in your journey as a developer!
# # But don't worry, I will explain how to do everything in the video tutorials on Udemy.
# from turtle import Turtle, Screen
#
# tutu = Turtle()
# print(tutu)
# tutu.shape("turtle")
# tutu.color("coral")
# tutu.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvwidth)
# print(my_screen.exitonclick())

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"], "l")
table.add_column("Type", ["Electric", "Water", "Fire"], "l")
# OR
table.align = "l"
print(table)
