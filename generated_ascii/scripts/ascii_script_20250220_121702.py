# Generated ASCII Art Script
# Created on: 2025-02-20 12:17:02

import os
import time
import random
import sys

# Get terminal size
def get_terminal_size():
    size = os.get_terminal_size()
    return size.lines, size.columns

# Color codes
colors = [
    "\033[38;5;{}m".format(i) for i in range(256)
]

# Create a diplay of animation frames
def create_frames(height, width):
    frames = []
    for _ in range(10):
        frame = []
        for i in range(height):
            line = "".join(colors[(i + _ * 10) % 256] + " " for _ in range(width))
            frame.append(line)
        frames.append(frame)
    return frames

# Display the frames
def display_frames(frames):
    try:
        while True:
            for frame in frames:
                sys.stdout.write("\033[H\033[J")  # Clear the terminal
                for line in frame:
                    sys.stdout.write(line + "\n")
                sys.stdout.flush()
                time.sleep(0.1)
    except KeyboardInterrupt:
        pass

# Main function
def main():
    height, width = get_terminal_size()
    frames = create_frames(height, width)
    display_frames(frames)

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    try:
        display_ascii_art()
    except KeyboardInterrupt:
        print("\033[0m\nAnimation stopped.")
