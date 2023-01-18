#Author: Christian Brewer
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

#gameboard
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-375, 0))
r_paddle = Paddle((375, 0))

ball = Ball()

l_score = Score(-75)
r_score = Score(75)

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "o")
screen.onkey(l_paddle.move_down, "q")

game = True
while game:
    screen.update()
    time.sleep(0.1)
    ball.move()
    ball_x = ball.xcor()
    ball_y = ball.ycor()
    #wall collision
    if ball_y > 280 or ball_y < -280:
        ball.bounce_y()

    #paddle collision
    if ball_x > 350 and ball_x < 360:
        if ball.distance(r_paddle) < 50:
            ball.bounce_x()
    elif ball_x < -350 and ball_x > -360:
        if ball.distance(l_paddle) < 50:

            ball.bounce_x()

    #detect score
    if ball_x > 400:
        ball.reset_ball()

    elif ball_x < -400:
        ball.reset_ball()
    

screen.exitonclick()