import os
import time
import subprocess

def clear_terminal():
    # Clear the terminal
    if os.name == 'nt':
        _ = subprocess.call('cls', shell=True)
    else:
        _ = subprocess.call('clear', shell=True)

# Define the animation frames
frames = [
    "\033[31m     *     \n"
    "\033[32m    ***    \n"
    "\033[33m   *****   \n"
    "\033[34m  *******  \n"
    "\033[35m ********* \n"
    "\033[36m***********\n",
    
    "\033[34m     *     \n"
    "\033[35m    ***    \n"
    "\033[31m   *****   \n"
    "\033[32m  *******  \n"
    "\033[33m ********* \n"
    "\033[36m***********\n",
    
    "\033[33m     *     \n"
    "\033[36m    ***    \n"
    "\033[34m   *****   \n"
    "\033[35m  *******  \n"
    "\033[31m ********* \n"
    "\033[32m***********\n",
    
    "\033[36m     *     \n"
    "\033[31m    ***    \n"
    "\033[32m   *****   \n"
    "\033[33m  *******  \n"
    "\033[34m ********* \n"
    "\033[35m***********\n"
]

while True:
    for frame in frames:
        clear_terminal()
        print(frame)
        time.sleep(0.5)  # Adjust the sleep time for speed of animation
