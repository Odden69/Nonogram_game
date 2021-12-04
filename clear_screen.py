"""
Clears the terminal

The code was found on
https://stackoverflow.com/questions/2084508/clear-terminal-in-python
"""
import os


def clear_screen():
    # os.system('cls' if os.name == 'nt' else 'clear')
    # os.system(clear-history)
    # os.system('cls||clear')
    # print(chr(27) + "[2J")
    os.system('printf "\ec"')
    # clear && printf '\e[3J'
    # print('\x1b[2J')
