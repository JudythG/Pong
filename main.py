from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

PADDLE_DISTANCE_FROM_CENTER = 350

screen = Screen()
screen.screensize(canvheight=600, canvwidth=800, bg="black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

right_paddle = Paddle((PADDLE_DISTANCE_FROM_CENTER, 0))
left_paddle = Paddle((-PADDLE_DISTANCE_FROM_CENTER, 0))
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if ball.distance(300, 400) > 110:
        ball.forward(5)

screen.exitonclick()
