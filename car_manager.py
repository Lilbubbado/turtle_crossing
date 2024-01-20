from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        new_car = Turtle()
        new_car.shape('square')
        new_car.shapesize(1, 2)
        new_car.color(COLORS[randint(0, len(COLORS) - 1)])
        new_car.penup()
        new_car.goto(290, randint(-250, 250))
        self.all_cars.append(new_car)

    def move(self):
        for x in range(0, len(self.all_cars) - 1):
            self.all_cars[x].back(self.speed)

    def next_level(self):
        self.speed += MOVE_INCREMENT

