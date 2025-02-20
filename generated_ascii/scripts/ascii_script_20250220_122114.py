# Generated ASCII Art Script
# Created on: 2025-02-20 12:21:14

import os
import time
import shutil
import sys
import itertools

# Color and constant definitions
colors = [
    "\033[30m", "\033[31m", "\033[32m", "\033[33m",
    "\033[34m", "\033[35m", "\033[36m", "\033[37m",
    "\033[40m", "\033[41m", "\033[42m", "\033[43m",
    "\033[44m", "\033[45m", "\033[46m", "\033[47m",
    "\033[0m"
]

WIDTH, HEIGHT = shutil.get_terminal_size()
FRAME_COUNT = 5

frames = []

def create_frame(frame_number):
    frame = []
    for y in range(HEIGHT):
        line = []
        for x in range(WIDTH):
            if (x // 4) % 2 == 0:
                char = ' '
            else:
                char = '*'
            
            # Apply color cycling
            color_choice = (x + frame_number) % len(colors)
            if y % 4 == 0:
                line.append(colors[color_choice] + char)
            else:
                line.append(colors[len(colors) - color_choice - 1] + char)
        frame.append(''.join(line))
    return frame

def setup_frames():
    for i in range(FRAME_COUNT):
        frames.append(create_frame(i))

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_frame(frame):
    clear_screen()
    sys.stdout.write('\n'.join(frame) + colors[-1])
    sys.stdout.flush()

def main():
    setup_frames()
    
    try:
        while True:
            for frame in frames:
                display_frame(frame)
                time.sleep(0.1)
    except KeyboardInterrupt:
        clear_screen()  # Cleanup on exit

if __name__ == "__main__":
    main()
