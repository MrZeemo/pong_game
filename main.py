from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.tracer(0)
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")

r_paddle = Paddle((375, 0))
l_paddle = Paddle((-375, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()



    if ball.distance(r_paddle) < 50 and ball.xcor() > 365 or ball.distance(l_paddle) < 50 and ball.xcor() < - 365:
        ball.bounce_paddle()



    if ball.xcor() > 389:
        ball.reset_position()
        scoreboard.score_l()

    if ball.xcor() < - 389:
        ball.reset_position()
        scoreboard.score_r()







screen.exitonclick()
