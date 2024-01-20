import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager, STARTING_MOVE_DISTANCE, MOVE_INCREMENT
from scoreboard import Scoreboard
from random import randint

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
scoreboard = Scoreboard()
cars = CarManager()

# Moves the turtle
screen.listen()
screen.onkey(turtle.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Generates cars
    num = randint(0, 100)
    if num % 3 == 0:
        cars.generate_car()
    cars.move()

    # Turtle crossed the road
    if turtle.ycor() >= FINISH_LINE_Y:
        turtle.crossed_the_road()
        scoreboard.level_up()
        cars.next_level()
        print(cars.speed)

    for x in range(0, len(cars.all_cars) - 1):
        if turtle.distance(cars.all_cars[x]) <= 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()