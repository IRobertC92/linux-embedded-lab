# Linux System Monitor CLI

A lightweight Linux CLI system monitor written in Python.  
Displays CPU, Memory, Disk usage, Network statistics, and a calculated Health Score (0–100).  
Includes trend indicators (↑, ↓, →) and optional CSV logging for historical analysis.

---

## Features

- Real-time CPU, Memory, Disk, Network monitoring.
- Health Score calculation based on CPU, Memory, and Disk usage.
- Colored trend indicators:
  - ↑ : metric increased
  - ↓ : metric decreased
  - → : metric stable
- Optional CSV logging.
- Optional JSON output.
- Optional per-core CPU usage display.

---

## Requirements

- Python 3.8+
- `psutil` library
- `rich` library

## Installation

Clone the repository:

```bash
git clone https://github.com/IRobertC92/linux-embedded-lab.git
cd linux-embedded-lab/python/sysmon-cli