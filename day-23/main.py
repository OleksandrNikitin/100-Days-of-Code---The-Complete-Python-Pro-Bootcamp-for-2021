import secrets
import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score_board = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(fun=player.move_up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if secrets.choice(range(1, 6)) == 1:
        car_manager.create_car()
    car_manager.move_cars()

    if player.ycor() > 280:
        player.reset_player()
        score_board.update_score()
        car_manager.increase_speed()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()
