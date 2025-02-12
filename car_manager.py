from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        randomize = random.randint(1,4)
        if randomize == 2:
            car = Turtle("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(1,2)
            random_y = random.randint(-250, 250)
            car.goto(300, random_y)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.backward(self.speed)

    def faster(self):
        self.speed += MOVE_INCREMENT
