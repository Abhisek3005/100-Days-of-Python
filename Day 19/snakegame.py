from turtle import *
import  time
from  snake import Snake
from  food import  Food
from  scoreboard import  Scoreboard

screen = Screen()
screen.setup(width=800,height=700)
screen.bgcolor("black")
screen.title("Abhisek's Snake Game")
screen.tracer(0) #this will help to off all the animation untill the use of update

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")




game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.11)
    snake.move()


    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()



    #Detect collision with wall
    if (
            snake.head.xcor() > 390
            or snake.head.xcor() < -390
            or snake.head.ycor() > 340
            or snake.head.ycor() < -340
    ):
        game_is_on = False
        scoreboard.game_over()



    #Detect collision with wtail

    # for segment in snake.segments:
    for segment in snake.segments[1:]:
    #     if segment == snake.head:
    #         pass

        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()









screen.exitonclick()