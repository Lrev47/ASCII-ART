# Generated ASCII Art Script
# Created on: 2025-02-20 11:59:14

import time
import os
import sys

# ANSI color codes
class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if sys.platform == 'win32' else 'clear')

def display_ascii_art():
    """Display the animated ASCII art"""
```python
import os
import time
import subprocess

def clear_terminal():
    # Clear the terminal
    if os.name == 'nt':
        _ = subprocess.call('cls', shell=True)
    else:
        _ = subprocess.call('clear', shell=True)

# Define the animation frames
frames = [
    "\033[31m     *     \n"
    "\033[32m    ***    \n"
    "\033[33m   *****   \n"
    "\033[34m  *******  \n"
    "\033[35m ********* \n"
    "\033[36m***********\n",
    
    "\033[34m     *     \n"
    "\033[35m    ***    \n"
    "\033[31m   *****   \n"
    "\033[32m  *******  \n"
    "\033[33m ********* \n"
    "\033[36m***********\n",
    
    "\033[33m     *     \n"
    "\033[36m    ***    \n"
    "\033[34m   *****   \n"
    "\033[35m  *******  \n"
    "\033[31m ********* \n"
    "\033[32m***********\n",
    
    "\033[36m     *     \n"
    "\033[31m    ***    \n"
    "\033[32m   *****   \n"
    "\033[33m  *******  \n"
    "\033[34m ********* \n"
    "\033[35m***********\n"
]

while True:
    for frame in frames:
        clear_terminal()
        print(frame)
        time.sleep(0.5)  # Adjust the sleep time for speed of animation
```

You can run this code in a Python environment that supports ANSI color codes and is capable of displaying terminal output.

if __name__ == "__main__":
    try:
        display_ascii_art()
    except KeyboardInterrupt:
        print(Colors.RESET + "\nAnimation stopped.")
