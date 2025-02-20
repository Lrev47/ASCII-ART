
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
