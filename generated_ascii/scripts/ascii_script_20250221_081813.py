# Generated ASCII Art Script
# Created on: 2025-02-21 08:18:13

import os
import shutil
import time
import sys

# ANSI color codes
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Define the frames for the animation
frames = [
    f"{RED}    @@@@@    {RESET}\n"
    f"{GREEN}   @@@@@@@   {RESET}\n"
    f"{YELLOW}  @@@@@@@@@  {RESET}\n"
    f"{BLUE} @@@@@@@@@@@ {RESET}\n"
    f"{MAGENTA} @@@@@@@@@@@ {RESET}\n"
    f"{CYAN}  @@@@@@@@@  {RESET}\n"
    f"{WHITE}   @@@@@@@   {RESET}\n"
    f"{RED}    @@@@@    {RESET}\n",

    f"{GREEN}    @@@@@    {RESET}\n"
    f"{YELLOW}   @@@@@@@   {RESET}\n"
    f"{BLUE}  @@@@@@@@@  {RESET}\n"
    f"{MAGENTA} @@@@@@@@@@@ {RESET}\n"
    f"{CYAN} @@@@@@@@@@@ {RESET}\n"
    f"{WHITE}  @@@@@@@@@  {RESET}\n"
    f"{RED}   @@@@@@@   {RESET}\n"
    f"{GREEN}    @@@@@    {RESET}\n"
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate():
    width, height = shutil.get_terminal_size()
    for frame in frames:
        clear_screen()
        print("\n" * ((height - len(frames[0].splitlines())) // 2))  # center vertically
        print(frame.center(width))  # center horizontally
        time.sleep(0.5)  # delay between frames

try:
    animate()
except KeyboardInterrupt:
    clear_screen()
    print(f"{RESET}Animation interrupted. Exiting...{RESET}")
    sys.exit(0)
finally:
    clear_screen()
    print(f"{RESET}Cleanup done. Goodbye!{RESET}")