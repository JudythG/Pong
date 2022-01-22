from turtle import Turtle

COLOR = "white"
SHAPE = "square"
STRETCH_WIDTH = 5
STRETCH_LENGTH = 1
UP = 90
DOWN = 270
MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, start_pos):
        super().__init__(shape=SHAPE)
        self.goto(start_pos)
        self.color(COLOR)
        self.shapesize(stretch_wid=STRETCH_WIDTH, stretch_len=STRETCH_LENGTH)
        self.penup()

    def up(self):
        new_y = self.ycor() + 20;
        self.goto(x = self.xcor(), y = new_y)

    def down(self):
        new_y = self.ycor() - 20;
        self.goto(x = self.xcor(), y = new_y)
