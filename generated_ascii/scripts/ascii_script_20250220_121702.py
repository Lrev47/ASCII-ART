# Generated ASCII Art Script
# Created on: 2025-02-20 12:17:02

import os
import time
import random
import sys
import math
from typing import List, Tuple

# ANSI color codes and styling
class Colors:
    # Foreground colors
    FG = {i: f"\033[38;5;{i}m" for i in range(256)}
    # Background colors
    BG = {i: f"\033[48;5;{i}m" for i in range(256)}
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"

# Animation configuration
FRAME_DELAY = 0.1
GRADIENT_SPEED = 0.1

def get_terminal_size() -> Tuple[int, int]:
    """Get current terminal size"""
    size = os.get_terminal_size()
    return size.lines - 1, size.columns  # Subtract 1 line for safety

def create_rainbow_gradient(width: int, offset: float = 0.0) -> List[int]:
    """Create a smooth rainbow gradient of given width"""
    colors = []
    for i in range(width):
        # Create a smooth color transition
        hue = (i / width + offset) % 1.0
        # Map hue to 256-color palette
        color_index = int((hue * 255) % 256)
        colors.append(color_index)
    return colors

def create_frame(height: int, width: int, time_offset: float) -> List[str]:
    """Create a single frame of the animation"""
    frame = []
    
    # Create different gradients for each row with phase shift
    for y in range(height):
        # Calculate row-specific offset for diagonal effect
        row_offset = time_offset + (y / height * 2)
        
        # Create gradient for this row
        fg_colors = create_rainbow_gradient(width, row_offset)
        bg_colors = create_rainbow_gradient(width, row_offset + 0.5)  # Offset for contrast
        
        # Build the row with both foreground and background colors
        row = ""
        for x in range(width):
            fg_color = Colors.FG[fg_colors[x]]
            bg_color = Colors.BG[bg_colors[x]]
            
            # Create interesting patterns using math functions
            char_index = int((math.sin(x/5 + time_offset*3) + math.cos(y/3 + time_offset*2)) * 4)
            chars = "▀▄█▓▒░ "  # Different ASCII chars for texture
            char = chars[char_index % len(chars)]
            
            row += f"{fg_color}{bg_color}{char}"
            
        frame.append(row)
    
    return frame

def clear_screen():
    """Clear the terminal screen"""
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def display_frame(frame: List[str]):
    """Display a single frame of the animation"""
    # Move cursor to top-left
    sys.stdout.write("\033[H")
    
    # Print each row
    for row in frame:
        sys.stdout.write(row + Colors.RESET + "\n")
    
    sys.stdout.flush()

def main():
    try:
        # Hide cursor
        sys.stdout.write("\033[?25l")
        
        # Clear screen initially
        clear_screen()
        
        # Animation loop
        time_offset = 0.0
        while True:
            # Get current terminal size
            height, width = get_terminal_size()
            
            # Create and display frame
            frame = create_frame(height, width, time_offset)
            display_frame(frame)
            
            # Update animation state
            time_offset += GRADIENT_SPEED
            
            # Control animation speed
            time.sleep(FRAME_DELAY)
            
    except KeyboardInterrupt:
        # Cleanup on exit
        sys.stdout.write(Colors.RESET)  # Reset colors
        sys.stdout.write("\033[?25h")   # Show cursor
        clear_screen()                   # Clear screen
        sys.stdout.write("\033[H")       # Move to top
        print("Animation stopped.")

if __name__ == "__main__":
    main()
