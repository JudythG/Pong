from turtle import Turtle

START_ANGLE = 40.5


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.penup()
        self.color("white")
        self.setheading(START_ANGLE)
