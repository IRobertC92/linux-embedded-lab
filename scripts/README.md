# 🧠Scripts

This folder contains small **utility scripts** used in the Linux Embedded Lab repository.  
They are intended to simplify common tasks such as cross-platform path conversion, automation, and workflow improvements.

---

## 🛠️ Included Scripts

### 💻`convert_path`
- **Version:** 1.1
- **Description:** Converts paths between Windows (`\`) and Linux/Git Bash (`/`) formats.
- **Features:**
  - Auto-detect environment (Linux, Git Bash/WSL, Windows CMD/PowerShell)
  - Clipboard integration (`xclip`, `wl-copy`, `pbcopy`, `clip.exe`)
  - Interactive mode, pipe support, and direct argument input
  - `--help` and `--version` flags
  - Normalizes drive letters (e.g., `D:Folder` → `D:/Folder`)

#### 🧩Usage Examples:
**Direct argument:**
```
convert_path "C:\\Users\\Robert"
# Output in Git Bash/Linux: C:/Users/Robert
# Output in Windows CMD: C:\Users\Robert
```

**Interactive mode:**
```
convert_path
Enter path: D:\Files\Work\Projects
# Output: D:/Files/Work/Projects (Git Bash)
```

**Pipe mode:**
```
echo "C:\Users\Docs" | convert_path
# Output: C:/Users/Docs
```

**Help and version:**
```
convert_path --help
convert_path --version
```
---

#### ⚙️ Installation
- Linux / WSL / Git Bash:
- sudo apt install dos2unix -y   # install dos2unix if not present
- dos2unix convert_path
- chmod +x convert_path.sh
- ./convert_path.sh

---

## ⚖️ License

This script is licensed under the MIT License.

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