#!/usr/bin/env bash
# convert_path.sh - Cross-platform path converter (Linux/Git Bash/WSL/Windows)
# Version: 1.4
# Author: Ionescu Robert-Constantin

VERSION="1.4"

# --- Helper: print help message ---
show_help() {
    cat <<EOF
Usage: $(basename "$0") [OPTIONS] [PATH]

Converts between Windows (\\) and Linux (/) path formats.
Normalizes drive letters (e.g., D:Folder -> D:/Folder).

Options:
  -h, --help        Show this help message and exit
  -v, --version     Show version information and exit

Examples:
  $(basename "$0") "C:\\Users\\Robert"
  $(basename "$0") "D:FilesWorkProjectsTrainings"
  echo "C:\\Users\\Robert" | $(basename "$0")
EOF
}

# --- Handle flags ---
case "$1" in
    -h|--help) show_help; exit 0 ;;
    -v|--version) echo "$(basename "$0") version $VERSION"; exit 0 ;;
esac

# --- Read input path ---
input="$1"
if [[ -z "$input" ]]; then
    if ! [ -t 0 ]; then
        read -r input
    else
        read -rp "Enter path: " input
    fi
fi

# --- Normalize drive letter ---
# Adds missing slash after drive letter if needed (e.g., D:Folder -> D:/Folder)
if [[ "$input" =~ ^([A-Za-z]):([^\\/].*)$ ]]; then
    input="${BASH_REMATCH[1]}:/${BASH_REMATCH[2]}"
fi

# --- Detect OS ---
if [[ "$OSTYPE" == "msys"* || "$OSTYPE" == "cygwin"* ]]; then
    target_os="gitbash"
elif [[ "$OSTYPE" == "win"* ]]; then
    target_os="windows"
else
    target_os="linux"
fi

# --- Convert path ---
case "$target_os" in
    gitbash|linux)
        # Always convert backslashes to forward slashes
        output=$(echo "$input" | sed 's|\\|/|g')
        ;;
    windows)
        # Windows native — convert / → \
        output="${input//\//\\}"
        ;;
esac

echo -e "\033[1;32mConverted path:\033[0m $output"

# --- Clipboard copy ---
if command -v xclip &>/dev/null; then
    echo -n "$output" | xclip -selection clipboard
    echo "(Copied to clipboard with xclip)"
elif command -v wl-copy &>/dev/null; then
    echo -n "$output" | wl-copy
    echo "(Copied to clipboard with wl-copy)"
elif command -v pbcopy &>/dev/null; then
    echo -n "$output" | pbcopy
    echo "(Copied to clipboard with pbcopy)"
elif command -v clip.exe &>/dev/null; then
    echo -n "$output" | clip.exe
    echo "(Copied to clipboard with Windows clip.exe)"
else
    echo "(No clipboard tool found — path printed only)"
fi