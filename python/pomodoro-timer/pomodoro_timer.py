#!/usr/bin/env python3
# =======================================================================================================================================================================
#  File        : pomodoro_timer.py
#  Author      : Ionescu Robert-Constantin
#  Date        : 2025-10-22
#  Version     : 1.0
#  Description : A Pomodoro timer GUI with optional sound alerts and configurable durations.
# =======================================================================================================================================================================
#  Usage       : python3 pomodoro_timer.py
# =======================================================================================================================================================================

import math
import os
import sys
import tkinter as tk
import argparse
import platform

# =======================================================================================================================================================================
# TO DO SECTION / Development Steps / Requirements
# ======================================================================================================================================================================= 

# TODO - STEP1 - Implement the PomodoroTimer class to encapsulate timer logic and UI handling.
#              - Store durations (work, short break, long break) and options (e.g., sound) as instance attributes.
#              - Initialize state variables such as 'reps' and 'timer'.

# TODO - STEP2 - Define the _setup_ui() method to create and configure the Tkinter UI.
#              - Set up the main window title, padding, and background color.
#              - Load the tomato image, canvas, and timer text.
#              - Create labels and buttons (Start, Reset, Check Marks) and place them in the grid layout.

# TODO - STEP3 - Implement the start_timer() method for controlling the Pomodoro cycle.
#              - Increase 'reps' and determine the current phase (Work / Short Break / Long Break).
#              - Call _set_title() to update the main label color and text.
#              - Start the countdown by calling _count_down() with the appropriate duration.

# TODO - STEP4 - Implement the _count_down() method for the recursive countdown mechanism.
#              - Update the timer display every second using Tkinter's after() method.
#              - When the countdown reaches zero, optionally play a sound and trigger start_timer() for the next phase.
#              - Update the check marks label after each completed work session.

# TODO - STEP5 - Implement the reset_timer() method to restore the initial state.
#              - Cancel any active countdown (after_cancel()).
#              - Reset timer text, label, and check marks.
#              - Clear 'reps' and ensure UI consistency.

# TODO - STEP6 - Implement command-line argument parsing using argparse.
#              - Support custom durations (--work, --short-break, --long-break) and the --sound flag.

# TODO - STEP7 - Add a play_sound() helper function for cross-platform audio notifications.
#              - Use winsound.Beep() on Windows and system bell (\a) on other OSes.

# TODO - STEP8 - Finalize the entry point: parse arguments, instantiate PomodoroTimer, and start the Tkinter main loop.

# =======================================================================================================================================================================
# Constants / Variables / Classes
# ======================================================================================================================================================================= 

COLORS = {
    "pink": "#FFB6C1",
    "red": "#FFA07A",
    "green": "#BDB76B",
    "yellow": "#F5F5DC",
}

FONT_NAME = "Calibri"

class PomodoroTimer:
    # Method to initialize the class and its elements
    def __init__(self, root: tk.Tk, work_min: int, short_break_min: int, long_break_min: int, sound: bool = False):
        self.work_min = work_min
        self.short_break_min = short_break_min
        self.long_break_min = long_break_min
        self.sound = sound

        self.reps = 0
        self.timer = None
        self.root = root
        self._setup_ui()

    # Method to create and configure the Tkinter UI elements
    def _setup_ui(self):
        self.root.title("Pomodoro Timer")
        self.root.config(padx=100, pady=50, bg=COLORS["yellow"])

        self.title_label = tk.Label(text="Timer", fg=COLORS["green"], bg=COLORS["yellow"], font=(FONT_NAME, 50))
        self.title_label.grid(column=1, row=0)

        image_path = os.path.join(os.path.dirname(__file__), "tomato.png")
        self.canvas = tk.Canvas(width=200, height=224, bg=COLORS["yellow"], highlightthickness=0)
        self.tomato_img = tk.PhotoImage(file=image_path)
        self.canvas.create_image(100, 112, image=self.tomato_img)
        self.timer_text = self.canvas.create_text(100, 130, text="00:00", fill="white",
                                                  font=(FONT_NAME, 35, "bold"))
        self.canvas.grid(column=1, row=1)

        tk.Button(text="Start", command=self.start_timer, highlightthickness=0).grid(column=0, row=2)
        tk.Button(text="Reset", command=self.reset_timer, highlightthickness=0).grid(column=2, row=2)

        self.check_marks = tk.Label(fg=COLORS["green"], bg=COLORS["yellow"])
        self.check_marks.grid(column=1, row=3)

    # Method to reset the timer to its initial state
    def reset_timer(self):
        if self.timer:
            self.root.after_cancel(self.timer)
        self.canvas.itemconfig(self.timer_text, text="00:00")
        self.title_label.config(text="Timer", fg=COLORS["green"])
        self.check_marks.config(text="")
        self.reps = 0

    # Method to start or continue the pomodoro cycle
    def start_timer(self):
        self.reps += 1
        work_sec = self.work_min * 60
        short_break_sec = self.short_break_min * 60
        long_break_sec = self.long_break_min * 60

        if self.reps % 8 == 0:
            self._set_title("Break", COLORS["red"])
            self._count_down(long_break_sec)
        elif self.reps % 2 == 0:
            self._set_title("Break", COLORS["pink"])
            self._count_down(short_break_sec)
        else:
            self._set_title("Work", COLORS["green"])
            self._count_down(work_sec)

    # Method to update the main label
    def _set_title(self, text, color):
        self.title_label.config(text=text, fg=color)

    # Method to count down recursively every second
    def _count_down(self, count):
        minutes = math.floor(count / 60)
        seconds = count % 60
        time_format = f"{minutes}:{seconds:02d}"
        self.canvas.itemconfig(self.timer_text, text=time_format)

        if count > 0:
            self.timer = self.root.after(1000, self._count_down, count - 1)
        else:
            if self.sound:
                play_sound()
            self.start_timer()
            marks = "✓" * (self.reps // 2)
            self.check_marks.config(text=marks)
        
# =======================================================================================================================================================================
# Helper Functions
# =======================================================================================================================================================================

# Function to play a simple notification sound if supported
def play_sound():
    try:
        if platform.system() == "Windows":
            import winsound
            winsound.Beep(1000, 300)  # frequency (Hz), duration (ms)
        else:
            sys.stdout.write("\a")
            sys.stdout.flush()
    except Exception:
        pass  # silently ignore if sound fails

# Function to parse command-line arguments
def parse_args():
    parser = argparse.ArgumentParser(description="Pomodoro Timer with optional sound alerts.")
    parser.add_argument("--work", type=int, default=25, help="Work session duration in minutes (default: 25)")
    parser.add_argument("--short-break", type=int, default=5, help="Short break duration in minutes (default: 5)")
    parser.add_argument("--long-break", type=int, default=20, help="Long break duration in minutes (default: 20)")
    parser.add_argument("--sound", action="store_true", help="Enable sound notifications")
    return parser.parse_args()

# =======================================================================================================================================================================
# Script Entry / Code Section / Main Loop
# =======================================================================================================================================================================

if __name__ == "__main__":
    args = parse_args()

    root = tk.Tk()
    PomodoroTimer(
        root,
        work_min=args.work,
        short_break_min=args.short_break,
        long_break_min=args.long_break,
        sound=args.sound
    )
    root.mainloop()