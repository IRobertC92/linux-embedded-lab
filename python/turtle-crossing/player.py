#!/usr/bin/env python3
# =======================================================================================================================================================================
#  File        : player.py
#  Author      : Ionescu Robert-Constantin
#  Date        : 2025-10-24
#  Version     : 1.0
#  Description : Player class for the Turtle Crossing Game.
# =======================================================================================================================================================================
#  Usage       : python3 player.py
# =======================================================================================================================================================================

from turtle import Turtle

# =======================================================================================================================================================================
# TO DO SECTION / Development Steps / Requirements
# ======================================================================================================================================================================= 

# TODO - STEP1 - Initialize the player turtle (shape, position, direction)
# TODO - STEP2 - Implement upward movement when pressing "Up"
# TODO - STEP3 - Detect when the player reaches the finish line
# TODO - STEP4 - Reset player to starting position when crossing is successful or game restarts

# =======================================================================================================================================================================
# Constants / Variables / Classes
# ======================================================================================================================================================================= 

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# Controllable turtle representing the player
class Player(Turtle):
    # Mehtod to initialize the player turtle at the starting position facing up
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    # Mehtod to Move the player upward by MOVE_DISTANCE
    def go_up(self) -> None:
        self.forward(MOVE_DISTANCE)

    # Mehtod to return True if the player has crossed the finish line
    def is_at_finish_line(self) -> bool:
        return self.ycor() > FINISH_LINE_Y

    # Mehtod to reset the player to the starting position
    def go_to_start(self) -> None:
        self.goto(STARTING_POSITION)