# Generated ASCII Art Script
# Created on: 2025-02-21 08:18:05

import os
import time
import shutil
import random

# ANSI color codes
RESET = "\033[0m"
COLORS = [
    "\033[31m",  # Red
    "\033[32m",  # Green
    "\033[33m",  # Yellow
    "\033[34m",  # Blue
    "\033[35m",  # Magenta
    "\033[36m",  # Cyan
    "\033[37m"   # White
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_frame(width, height):
    frame = []
    for _ in range(height):
        line = ''.join(random.choice(COLORS) + random.choice([' ', '*', '.', 'o']) for _ in range(width))
        frame.append(line + RESET)
    return frame

def animate():
    try:
        while True:
            width, height = shutil.get_terminal_size()
            frame = generate_frame(width, height)
            clear_screen()
            print('\n'.join(frame))
            time.sleep(0.1)
    except KeyboardInterrupt:
        clear_screen()
        print("Animation stopped. Exiting...")

if __name__ == "__main__":
    animate()