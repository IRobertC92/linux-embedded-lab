# 🐧Linux + 🐍Python Useful Commands

🔎 Check the Python version
python3 --version
python --version

🔎 Check where packages are installed
python3 -m site
python3 -m pip show pip

🔄 Upgrade pip
python3 -m pip install --upgrade pip

🔄 Update a single package
python3 -m pip install --upgrade requests

🔄 Update all installed packages
python3 -m pip list --outdated
python3 -m pip list --outdated | tail -n +3 | awk '{print $1}' | xargs -n1 python3 -m pip install -U #update all automatically

🔄 If you installed Python packages via APT
sudo apt install python3-requests

- Then update them via apt, not pip
sudo apt update # refresh package lists
sudo apt upgrade  # upgrade all packages, including python3-requests

🔎 Check the installed version
python3 -m pip show requests

⚙️ View all Python processes
ps aux | grep python
#the second column (e.g., 1234, 5678) is the PID (process ID)
kill PID

#safely stop only your script (e.g. my_script.py)
pkill -f my_script.py