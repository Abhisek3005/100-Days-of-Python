
from turtle import Turtle

STARTING_POSITIOn = [(0,0), (-20,0), (-40,0)]
move_distance  = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIOn:
           self.add_segment(position)
        # for position in STARTING_POSITIOn:
        #     segment_1 = Turtle(shape="square")
        #     segment_1.color("white")
        #     segment_1.penup()
        #     segment_1.goto(position)
        #     self.segments.append(segment_1)

    def add_segment(self,position):

            segment_1 = Turtle(shape="square")
            segment_1.color("white")
            segment_1.penup()
            segment_1.goto(position)
            self.segments.append(segment_1)

    def extend(self):

       # add a new degment to the snake
       self.add_segment(self.segments[-1].position())



    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, - 1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(move_distance)

    def up(self):
        if self.head.heading() != DOWN:
          self.head.setheading(UP)



    def down(self):

        if self.head.heading() != UP:
          self.head.setheading(DOWN)



    def right(self):

        if self.head.heading() != LEFT:
          self.head.setheading(RIGHT)

    def left(self):

        if self.head.heading() != RIGHT:
           self.head.setheading(LEFT)










