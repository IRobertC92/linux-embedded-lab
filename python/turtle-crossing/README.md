# 🐢 Turtle Crossing Deluxe (Python + Turtle GUI)

A fun and interactive Turtle Crossing Game built with Python's Turtle module. 
Guide your turtle safely across busy lanes of traffic, level up, and enjoy optional sound effects for crossings and game over events.

---

## Features

🛣️ **Turtle Adventure** — move your turtle from the bottom to the top of the screen.  
- ⚡ **Increasing Difficulty** — cars speed up every time you successfully cross.  
- 🔊 **Optional Sound Effects** — hear a sound when leveling up or game over occurs.  
- 🎮 **Keyboard Controls** — Up arrow to move, P to pause, R to restart.  
- 📊 **Scoreboard & Levels** — track your progress with a visible level indicator.  
- 💻 **Cross-Platform** — works on Windows, macOS, and Linux with Python 3.  

---

## 🧩 Installation
Clone the repository:

```bash
git clone https://github.com/IRobertC92/linux-embedded-lab.git
cd linux-embedded-lab/python/turtle-crossing
```

---

## 🏃 Usage and Controls
- python main.py
- Up Arrow → Move the turtle forward
- P → Pause / Resume the game
- R → Restart the game after Game Over

---

## 🔊 Sound Effects
- Level Up — plays when the turtle successfully crosses
- Game Over — plays when the turtle collides with a car
- Sounds are optional. If missing, the game runs silently.
- You can replace or add .wav files in the sounds/ folder for customization.

---

## 🧠 How It Works
- The turtle starts at the bottom of the screen.
- Cars are randomly generated and move left across the screen.
- Collision with a car triggers Game Over.
- Reaching the top increases the level and the speed of cars.
- The game continues indefinitely, challenging the player as levels increase.

---

## ⚙️ Project Structure
Py_Turtle_Crossing_Game/
│
├─ main.py          # Main game loop
├─ player.py        # Turtle player class
├─ manager.py       # Car management and movement
├─ score.py         # Scoreboard display
├─ sound.py         # SoundManager for levelup/gameover sounds
├─ sounds/          # Folder for .wav sound files
└─ tests/           # Unit tests for each module

---

## 🧪 Testing
pytest -v

---

## ⚖️ License

This project is licensed under the MIT License.

MIT License

Copyright (c) 2025 Ionescu Robert-Constantin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.