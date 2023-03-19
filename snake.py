from turtle import Turtle, Screen
import time
scr = Screen()

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]

class Snake:
    def __init__(self):
        tim = Turtle("square")
        tim.speed("fastest")
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # for i in range(3):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        # x = (-20 * (i + 1))
        # tim.goto(x, 0)
        tim.goto(position)
        self.segments.append(tim)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_no in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_no - 1].xcor()
            new_y = self.segments[seg_no - 1].ycor()
            self.segments[seg_no].goto(new_x, new_y)
        self.segments[0].forward(20)
        # self.segments[0].left(90)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(0)
