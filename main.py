#Author: Christian Brewer
from turtle import Turtle, Screen
from paddle import Paddle
import time

#gameboard
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-375, 0))
r_paddle = Paddle((375, 0))

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "o")
screen.onkey(l_paddle.move_down, "q")

game = True
while game:
    screen.update()
    time.sleep(0.08)

screen.exitonclick()