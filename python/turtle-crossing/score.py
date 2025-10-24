#!/usr/bin/env python3
# =======================================================================================================================================================================
#  File        : score.py
#  Author      : Ionescu Robert-Constantin
#  Date        : 2025-10-24
#  Version     : 1.0
#  Description : Scoreboard for the Turtle Crossing Game that displays level, messages and game-over info.
# =======================================================================================================================================================================
#  Usage       : python3 score.py
# =======================================================================================================================================================================

from turtle import Turtle

# =======================================================================================================================================================================
# TO DO SECTION / Development Steps / Requirements
# ======================================================================================================================================================================= 

# TODO - STEP1 - Initialize scoreboard with level 1 and setup font and position
# TODO - STEP2 - Display current level in top-left corner
# TODO - STEP3 - Increase level and refresh text on screen when player succeeds
# TODO - STEP4 - Show Game Over message when collision occurs
# TODO - STEP5 - Display temporary text such as PAUSED
# TODO - STEP6 - Reset scoreboard when restarting the game

# =======================================================================================================================================================================
# Constants / Variables / Classes
# ======================================================================================================================================================================= 

FONT = ("Courier", 24, "normal")
SMALL_FONT = ("Courier", 18, "normal")

# Displays the current level and game messages for the Turtle Crossing Game
class Score(Turtle):
    # Method to initialize the scoreboard at the top-left corner with level 1
    def __init__(self) -> None:
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    # Method to refresh the displayed level
    def update_scoreboard(self) -> None:
        self.clear()
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    # Method to increase the level and update the scoreboard
    def increase_level(self) -> None:
        self.level += 1
        self.update_scoreboard()

    # Method to display 'GAME OVER' message and restart hint in the center of the screen
    def game_over(self) -> None:
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
        self.goto(0, -30)
        self.write("Press R to restart", align="center", font=SMALL_FONT)

    # Method to display a temporary message like 'PAUSED' in the center of the screen
    def show_message(self, text: str) -> None:
        self.clear()
        self.goto(0, 0)
        self.write(text, align="center", font=FONT)

    # Method to reset scoreboard for a new game
    def reset(self) -> None:
        self.level = 1
        self.update_scoreboard()