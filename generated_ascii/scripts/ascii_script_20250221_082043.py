# Generated ASCII Art Script
# Created on: 2025-02-21 08:20:43

import os
import time
import shutil
import math

# ANSI Color Codes
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_terminal_size():
    return shutil.get_terminal_size()

def generate_frame(frame_number, width, height):
    result = ""
    center_x, center_y = width // 2, height // 2
    radius = min(width, height) // 4
    angle_increment = 2 * math.pi / 20  # 20 points in the circle

    for y in range(height):
        for x in range(width):
            distance = math.sqrt((x - center_x)**2 + (y - center_y)**2)
            if radius - 1 <= distance <= radius + 1:
                char = "|"
                if frame_number % 2 == 0:
                    char = RED + "*" + RESET
                else:
                    char = GREEN + "*" + RESET
                result += char
            else:
                result += " "
        result += "\n"
    return result

def main():
    try:
        while True:
            width, height = get_terminal_size()
            for frame_number in range(2):  # Two frames only
                clear_screen()
                frame = generate_frame(frame_number, width, height)
                print(frame)
                time.sleep(0.5)
    except KeyboardInterrupt:
        clear_screen()
        print(RESET + "Animation stopped. Cleaning up..." + RESET)
        exit(0)

if __name__ == "__main__":
    main()