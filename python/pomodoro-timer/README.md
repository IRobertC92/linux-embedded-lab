# 🕒 Pomodoro Timer (Tkinter GUI)

A clean, customizable Pomodoro Timer built with Python and Tkinter — designed to help you stay focused during work sessions and take regular breaks.
Includes configurable durations, visual progress tracking, and optional sound alerts when sessions change.

---

## 🚀 Features

🧭 Work/Break Cycles — follows the Pomodoro technique automatically

- ⚙️ Custom Durations — set work, short break, and long break times from the command line

- 🔊 Optional Sound Alerts — get notified when sessions end

- 🎨 Simple GUI — built with Tkinter, using a tomato image and soft colors

- ✅ Visual Progress — adds a ✓ mark after each completed work session

- 💻 Cross-Platform — works on Windows, macOS, and Linux

---

## 🧩 Installation
Clone the repository:

```bash
git clone https://github.com/IRobertC92/linux-embedded-lab.git
cd linux-embedded-lab/python/pomodoro-timer
```

---

## 🏃 Usage
- Basic run
- python3 pomodoro_timer.py

- Custom durations
- python3 pomodoro_timer.py --work 30 --short-break 10 --long-break 25

- With sound alerts
- python3 pomodoro_timer.py --sound

---

## ⚙️ Command-Line Options
- Option	Description	Default
- --work	Work session duration (minutes)	25
- --short-break	Short break duration (minutes)	5
- --long-break	Long break duration (minutes)	20
- --sound	Play sound alerts when session changes	Off

---

## 🧠 How It Works
- The timer cycles through the following sequence automatically:

- Work (25 min)
- Short Break (5 min)
- Work (25 min)
- Short Break (5 min)
- Work (25 min)
- Short Break (5 min)
- Work (25 min)
- Long Break (20 min)

- After the long break, the cycle restarts.
- Each completed work session adds a ✓ mark under the timer.

---

## 🔔 Sound Notifications
- If you run with --sound:
- On Windows, it uses the winsound.Beep() function.
- On macOS/Linux, it triggers the system bell (\a).
- You can easily replace the play_sound() function in the script with another sound method (e.g., playsound or pygame.mixer) if you want custom audio.

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