# Generated ASCII Art Script
# Created on: 2025-02-21 08:29:56

import os
import time
import shutil
import sys

# ANSI color codes
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"

# Frame generator for a bouncing ball animation
def generate_frames(width, height):
    frames = []
    ball_positions = [(x, 1) for x in range(1, width - 1)]
    
    for bounce in range(6):
        for x in ball_positions:
            frame = [[" "] * width for _ in range(height)]
            frame[x[1]][x[0]] = "O"
            for j in range(height):
                if j == height - 1:
                    frame[j] = frame[j][:1] + ["-"] * (width - 2) + frame[j][-1:]
            frames.append(frame)
        if bounce % 2 == 0:
            ball_positions = [(x, 2) for x in range(1, width - 1)]
        else:
            ball_positions = [(x, 3) for x in range(1, width - 1)]
    
    return frames

# Function to print a frame
def print_frame(frame):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in frame:
        print("".join(row))
    sys.stdout.flush()

# Main animation logic
def animate():
    terminal_size = shutil.get_terminal_size()
    width, height = terminal_size.columns, terminal_size.lines
    frames = generate_frames(width, height - 2)

    try:
        while True:
            for frame in frames:
                print_frame(frame)
                time.sleep(0.1)
    except KeyboardInterrupt:
        print(RESET + "\nAnimation stopped.")

if __name__ == "__main__":
    animate()