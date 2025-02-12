import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
scoreboard = Scoreboard()

car_manager = CarManager()

screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    #reset position if reach the finish line and upgrade level score
    if player.reach_finish():
        player.go_to_start()
        car_manager.faster()
        player.faster()
        scoreboard.level_up()

    #detect collision with the cars
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.is_Game_Over()

screen.exitonclick()