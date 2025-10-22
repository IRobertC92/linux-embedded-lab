# 🐍 Python Utilities — Linux Embedded Lab

This folder contains Python-based lab projects and small utilities developed as part of the **linux-embedded-lab** repository.  
Each subproject is self-contained, testable, and focuses on a specific concept or tool.

---

## 📁 Folder Structure

python/
│
├── morse_code/
│ ├── morse_code_decode.py
│ ├── test_morse_pytest.py
│ ├── test_morse_unittest.py
│ └── README.md
│
└── sysmon-cli/
├── sysmon_cli.py
├── test_sysmon_cli.py
└── README.md

pgsql
Copy code

---

## 🔤 morse_code

A simple **Morse code encoder/decoder** implemented in Python.  
It converts user input text into Morse code and can decode it back into plain text.

### Features
- Bidirectional conversion (text ↔ Morse)
- Interactive CLI input/output
- Unit tests with `pytest`

### Run
```bash
python morse_code_decode.py
Test
bash
Copy code
pytest test_morse_pytest.py
```

## 💻 sysmon-cli
A system monitor CLI tool that displays real-time system stats such as CPU, memory, disk, and network usage.

### Features
- Uses psutil for system metrics
- Colored terminal output with rich
- Supports per-core CPU stats
- Tested with pytest and mock objects

###Run
```bash
Copy code
python sysmon_cli.py
Test
bash
Copy code
pytest test_sysmon_cli.py
```

## 🧩 Development Notes
Python ≥ 3.10 recommended
Each project is independent — no shared imports
Unit tests use pytest and unittest.mock
Folder naming follows lowercase-with-hyphens convention for clarity

## 📜 License
This repository is for learning and experimental purposes.
Feel free to fork, modify, and experiment.