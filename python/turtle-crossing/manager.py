#!/usr/bin/env python3
# =======================================================================================================================================================================
#  File        : manager.py
#  Author      : Ionescu Robert-Constantin
#  Date        : 2025-10-24
#  Version     : 1.0
#  Description : Manager for the Turtle Crossing Game, handles car creation and movement.
# =======================================================================================================================================================================
#  Usage       : python3 manager.py
# =======================================================================================================================================================================

from turtle import Turtle
import random

# =======================================================================================================================================================================
# TO DO SECTION / Development Steps / Requirements
# ======================================================================================================================================================================= 

# TODO - STEP1 - Define car appearance and movement parameters (colors, speed, spacing)
# TODO - STEP2 - Create a Manager class to store and control all car instances
# TODO - STEP3 - Implement random car generation avoiding top/bottom safe zones
# TODO - STEP4 - Move all cars leftward at current car speed each game tick
# TODO - STEP5 - Increase car speed when the player levels up
# TODO - STEP6 - Provide reset functionality to clear cars on restart

# =======================================================================================================================================================================
# Constants / Variables / Classes
# ======================================================================================================================================================================= 

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
CAR_SPAWN_CHANCE = 6  # smaller = more frequent
SAFE_ZONE_Y = 50       # Top and bottom safe zone in pixels
SCREEN_HEIGHT = 600

# Manages all cars in the Turtle Crossing Game
class Manager:
    # Method to initialize the class and its members
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    # Method to create all cars
    def create_car(self):
        if random.randint(1, CAR_SPAWN_CHANCE) == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            
            min_y = -SCREEN_HEIGHT // 2 + SAFE_ZONE_Y
            max_y = SCREEN_HEIGHT // 2 - SAFE_ZONE_Y
            random_y = random.randint(min_y, max_y)
            
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    # Method to move all cars leftward by the current car speed
    def move_car(self):
        """Move all cars leftward by the current car speed."""
        for car in self.all_cars:
            car.backward(self.car_speed)

    # Method to increase the speed of all cars (called on level up)
    def level_up(self):
        self.car_speed += MOVE_INCREMENT

    # Method to hide and remove all cars (called on game restart)
    def reset(self):
        for car in self.all_cars:
            car.hideturtle()
        self.all_cars.clear()
        self.car_speed = STARTING_MOVE_DISTANCE
