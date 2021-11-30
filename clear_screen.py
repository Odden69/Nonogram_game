"""
Clears the terminal

The code was found on
https://stackoverflow.com/questions/2084508/clear-terminal-in-python
"""
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
