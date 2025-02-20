# Generated ASCII Art Script
# Created on: 2025-02-20 12:08:38

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

# Clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ANSI color codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
PURPLE = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"

# Define the frames of the animation
frames = [
    f"""
{CYAN}  .-~~-.     
{GREEN} (       )    
{YELLOW}  `-.__.-'       
{RESET}           
    """,
    f"""
{RED}  .-~~-.     
{BLUE} (       )    
{PURPLE}  `-.__.-'       
{RESET}           
    """,
    f"""
{YELLOW}  .-~~-.     
{CYAN} (       )    
{GREEN}  `-.__.-'       
{RESET}           
    """,
    f"""
{BLUE}  .-~~-.     
{PURPLE} (       )    
{RED}  `-.__.-'       
{RESET}           
    """,
]

# Main animation loop
while True:
    for frame in frames:
        clear_screen()
        print(frame)
        time.sleep(0.5)
```

To run the above code, copy it to a Python environment that supports ANSI color codes in the terminal, and execute it. The animation will display a colorful bouncing ball effect with changing colors across the frames.

if __name__ == "__main__":
    try:
        display_ascii_art()
    except KeyboardInterrupt:
        print(Colors.RESET + "\nAnimation stopped.")
