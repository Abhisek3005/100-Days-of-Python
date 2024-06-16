from  turtle import  *
tim = Turtle()
def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)

def move_c_clockwise():
    tim.left(10)

def move_clockwise():
    tim.right(10)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def move_forward():
    tim.forward(10)
screen = Screen()
screen.listen() #this llisten is used to do something on pressing some keys
screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "S", fun = move_backward)
screen.onkey(key = "a", fun = move_c_clockwise)
screen.onkey(key = "d", fun = move_clockwise)
screen.onkey(key = "c ", fun = clear_drawing)
screen.exitonclick()