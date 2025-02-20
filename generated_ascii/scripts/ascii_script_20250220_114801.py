# Generated ASCII Art Script
# Created on: 2025-02-20 11:48:01

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
    EYES_OPEN_FACE = """
    ^_^
    """

    EYES_CLOSED_FACE = """
    -_-
    """
    
    colors = [Colors.RED, Colors.GREEN, Colors.YELLOW, 
             Colors.BLUE, Colors.PURPLE, Colors.CYAN]
    
    try:
        while True:
            for color in colors:
                clear_screen()
                print(f"{color}{EYES_OPEN_FACE}{Colors.RESET}", end="")
                time.sleep(0.5)
                
                clear_screen()
                print(f"{color}{EYES_CLOSED_FACE}{Colors.RESET}", end="")
                time.sleep(0.5)
    except KeyboardInterrupt:
        print(Colors.RESET + "\nAnimation stopped.")

if __name__ == "__main__":
    display_ascii_art()
