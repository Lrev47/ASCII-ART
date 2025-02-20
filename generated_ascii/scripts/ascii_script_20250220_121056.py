
import os
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

frames = [
    f"""
    {CYAN}      ^    {RESET}
    {GREEN}     / \\   {RESET}
    {YELLOW}    /   \\  {RESET}
    {RED}   /     \\ {RESET}
    {MAGENTA}  /       \\{RESET}
    {WHITE} /_________\\{RESET}
    """,
    f"""
    {MAGENTA}      ^    {RESET}
    {YELLOW}     / \\   {RESET}
    {RED}    /   \\  {RESET}
    {GREEN}   /     \\ {RESET}
    {CYAN}  /       \\{RESET}
    {WHITE} /_________\\{RESET}
    """,
    f"""
    {RED}      ^    {RESET}
    {MAGENTA}     / \\   {RESET}
    {CYAN}    /   \\  {RESET}
    {YELLOW}   /     \\ {RESET}
    {GREEN}  /       \\{RESET}
    {WHITE} /_________\\{RESET}
    """,
]

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

try:
    while True:
        for frame in frames:
            clear_terminal()
            print(frame)
            time.sleep(0.5)
except KeyboardInterrupt:
    clear_terminal()
    sys.exit(0)
