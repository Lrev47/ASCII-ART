# Generated ASCII Art Script
# Created on: 2025-02-20 12:13:19

import os
import time

frames = [
    "\033[31m(\033[33m*\033[31m)\033[0m",
    "\033[33m(\033[32m*\033[33m)\033[0m",
    "\033[32m(\033[34m*\033[32m)\033[0m",
    "\033[34m(\033[35m*\033[34m)\033[0m",
    "\033[35m(\033[36m*\033[35m)\033[0m",
    "\033[36m(\033[31m*\033[36m)\033[0m"
]

try:
    while True:
        for frame in frames:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(frame)
            time.sleep(0.2)
except KeyboardInterrupt:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Animation stopped.")

if __name__ == "__main__":
    try:
        display_ascii_art()
    except KeyboardInterrupt:
        print("\033[0m\nAnimation stopped.")
