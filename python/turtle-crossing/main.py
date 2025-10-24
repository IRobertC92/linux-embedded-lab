#!/usr/bin/env python3
# =======================================================================================================================================================================
#  File        : main.py
#  Author      : Ionescu Robert-Constantin
#  Date        : 2025-10-24
#  Version     : 1.0
#  Description : Main game loop for the Turtle Crossing Game.
# =======================================================================================================================================================================
#  Usage       : python3 main.py
# =======================================================================================================================================================================

from turtle import Screen
from player import Player
from manager import Manager
from score import Score
from playsound import playsound
from sound import SoundManager
import time
import os

# =======================================================================================================================================================================
# TO DO SECTION / Development Steps / Requirements
# ======================================================================================================================================================================= 
# TODO - STEP1 - Setup the game screen (size, title, tracer off for manual updates)
# TODO - STEP2 - Initialize core objects: Player, Manager, Score, SoundManager
# TODO - STEP3 - Load sound effects and handle missing files gracefully
# TODO - STEP4 - Define helper functions: pause toggle, restart, and main game loop
# TODO - STEP5 - Game loop updates cars, checks collisions, handles level-up logic
# TODO - STEP6 - Bind keyboard inputs: Up = move, P = pause, R = restart
# TODO - STEP7 - Run main game loop and wait for user exit

# =======================================================================================================================================================================
# Constants / Variables / Classes
# ======================================================================================================================================================================= 

SOUND_ENABLED = True         # Toggle sound effects
REFRESH_RATE = 0.1           # Game speed (smaller = faster)
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# =======================================================================================================================================================================
# Helper Functions
# =======================================================================================================================================================================

# Function to detect pause and toggle it via the game
def toggle_pause():
    global paused
    paused = not paused
    if paused:
        scoreboard.show_message("PAUSED")
    else:
        scoreboard.update_scoreboard()

# Function to restart the game and resets everything
def restart_game():
    global paused, player, car_manager, scoreboard
    paused = False

    # hide and remove the old turtle before creating a new one
    player.hideturtle()
    del player  # optional cleanup (not mandatory but clean)

    # Recreate fresh game objects
    player = Player()
    car_manager.reset()
    scoreboard.reset()

    # Re-bind key controls to the new player
    screen.onkey(None, "Up")  # clear previous binding
    screen.onkey(player.go_up, "Up")

    # Resume the main loop
    game_loop()

# Main function loop
def game_loop():
    global paused
    game_is_on = True
    while game_is_on:
        if paused:
            screen.update()
            time.sleep(0.1)
            continue

        time.sleep(REFRESH_RATE)
        screen.update()
        car_manager.create_car()
        car_manager.move_car()

        # Detect collision with car
        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                scoreboard.game_over()
                if SOUND_ENABLED:
                    sound_manager.play("gameover")
                game_is_on = False
                break

        # Detect successful crossing
        if player.is_at_finish_line():
            player.go_to_start()
            car_manager.level_up()
            scoreboard.increase_level()
            if SOUND_ENABLED:
                sound_manager.play("levelup")

    # Disable movement after game over
    screen.onkey(None, "Up")

# =======================================================================================================================================================================
# Script Entry / Code Section / Main Loop
# =======================================================================================================================================================================

# Initialize screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)
screen.title("🐢 Turtle Crossing Deluxe 🏎️")

# Initialize game objects
player = Player()
car_manager = Manager()
scoreboard = Score()
paused = False

# Initialize sounds
sound_manager = SoundManager()
current_dir = os.path.dirname(__file__)

try:
    levelup_sound = sound_manager.load_sound("levelup", os.path.join(current_dir, "sounds", "levelup.wav"))
    gameover_sound = sound_manager.load_sound("gameover", os.path.join(current_dir, "sounds", "gameover.wav"))
except FileNotFoundError as e:
    print("Warning:", e)
    SOUND_ENABLED = False  # disable sounds if files are missing

# Control bindings
screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(toggle_pause, "p")
screen.onkey(restart_game, "r")

# Start the game
game_loop()
screen.exitonclick()