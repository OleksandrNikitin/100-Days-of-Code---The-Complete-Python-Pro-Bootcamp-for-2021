import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun=left_paddle.move_up, key="w")
screen.onkey(fun=left_paddle.move_down, key="s")
screen.onkey(fun=right_paddle.move_up, key="Up")
screen.onkey(fun=right_paddle.move_down, key="Down")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    elif ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    elif ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    elif ball.xcor() > 340:
        scoreboard.increase_left_score()
        ball.reset_position()

    elif ball.xcor() < -340:
        scoreboard.increase_right_score()
        ball.reset_position()

    ball.move()
    screen.update()

screen.exitonclick()
