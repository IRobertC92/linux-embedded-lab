#!/usr/bin/env python3
# =======================================================================================================================================================================
#  File        : sound.py
#  Author      : Ionescu Robert-Constantin
#  Date        : 2025-10-24
#  Version     : 1.0
#  Description : Handles sound loading and playback for the Turtle Crossing Game.
# =======================================================================================================================================================================
#  Usage       : python3 sound.py
# =======================================================================================================================================================================

import os
import pygame

# =======================================================================================================================================================================
# TO DO SECTION / Development Steps / Requirements
# ======================================================================================================================================================================= 

# TODO - STEP1 - Initialize pygame mixer safely
# TODO - STEP2 - Define a dictionary to store loaded sounds
# TODO - STEP3 - Implement sound loading with path normalization and file existence check
# TODO - STEP4 - Implement play() method with optional looping
# TODO - STEP5 - Handle missing sounds or playback errors gracefully in main.py

# =======================================================================================================================================================================
# Constants / Variables / Classes
# ======================================================================================================================================================================= 

# Manages loading and playing sound effects using pygame
class SoundManager:
    # Method to initialize the pygame mixer and sound dictionary
    def __init__(self) -> None:
        pygame.mixer.init()
        self.sounds: dict[str, pygame.mixer.Sound] = {}

    # Method to load a sound file and store it in the dictionary
    def load_sound(self, name: str, filename: str) -> pygame.mixer.Sound:
        current_dir = os.path.dirname(__file__)
        sound_path = os.path.normpath(os.path.join(current_dir, filename))

        if not os.path.exists(sound_path):
            raise FileNotFoundError(f"Sound file not found: {sound_path}")
        
        sound = pygame.mixer.Sound(sound_path)
        self.sounds[name] = sound
        return sound

    # Method to play a loaded sound by name
    def play(self, name: str, loop: bool = False) -> None:
        if name not in self.sounds:
            raise ValueError(f"Sound '{name}' not loaded")
        loops = -1 if loop else 0
        self.sounds[name].play(loops=loops)