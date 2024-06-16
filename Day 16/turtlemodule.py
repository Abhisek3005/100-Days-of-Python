#import turtle
# timmy = turtle.Turtle()
#Turtle and screen are the classes
from turtle import Turtle,Screen
timmy = Turtle()
print(timmy)
timmy.shape("triangle")
timmy.color("coral")
timmy.forward(100.98)
my_screen = Screen()
#my_scrren is the object and canvheight is the attribute
print(my_screen.canvheight)
#exitonclick is the method
my_screen.exitonclick()  