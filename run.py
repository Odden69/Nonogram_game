"""
Runs the game with the start menu and fills the player and
game patterns with default values
"""
import random
import game_board
import game_entry
from clear_screen import clear_screen


def print_start_menu():
    """
    Prints the start message to the terminal
    """
    clear_screen()
    message = '''Welcome to the Nonogram game!\n
        Choose one the following options by typing the number.\n
        1. How to play.\n
        2. Play Game\n'''
    print(message)
    players_choice_start_menu()


def players_choice_start_menu():
    """
    Gets start menu input from player
    """
    while True:
        try:
            choice = int(input('Make your choice: '))
        except ValueError:
            print('        That was not a number. Please try again.')
        else:
            if choice == 1:
                print_how_to_play()
            elif choice == 2:
                break
            else:
                print('       That was not a valid choice, please type 1 or 2')


def print_how_to_play():
    """
    Prints info on how to play the game to the terminal
    """
    clear_screen()
    print('        This is how to play')
    input('Press any key to go back to main menu: ')
    print_start_menu()


def get_board_size_from_player():
    """
    Gets board size input from player
    """
    while True:
        try:
            size = int(input('Choose your preferred board size. '
                             'Enter a number between 4 and 20: '))
        except ValueError:
            print('        That was not a number. Please try again.')
        else:
            if size >= 4 and size <= 20:
                break
            else:
                print('That was not a valid choice, please enter a number '
                      'between 4 and 20')
    return size


def populate_game_pattern(size):
    """
    populates the game board matrix with random 0s and 1s.
    0 for empty and 1 for a filled index.
    """
    game_pattern = [[str(random.randint(0, 1)) for i in range(size)]
                    for j in range(size)]
    return game_pattern


def populate_player_pattern(size):
    """
    populates the players board matrix with a single dot for each index.
    """
    player_pattern = []
    player_pattern = [[chr(183) for i in range(size)] for j in range(size)]
    return player_pattern


def play_game(size, player_pattern, game_pattern):
    """
    Prints the board and gets new game input from player until the game
    is finished or the player aborts.
    """
    while True:
        clear_screen()
        game_board.print_game_board(size, player_pattern, game_pattern)
        player_pattern = \
            game_entry.get_board_input_from_player(size, player_pattern,
                                                   game_pattern)


def restart_game(size, game_pattern):
    """
    Restarts the game with the same game_pattern as the game before
    The main condition was found on
    https://stackoverflow.com/questions/31031503/import-a-python-module-without-running-it
    """
    print('\nYou chose to replay the game to try to solve the same \
pattern again.\nGood luck!\n')
    input('Press any key to continue: ')
    player_pattern = populate_player_pattern(size)
    play_game(size, player_pattern, game_pattern)


def run_game():
    """
    Runs the application.
    """
    print_start_menu()
    size = get_board_size_from_player()
    game_pattern = populate_game_pattern(size)
    player_pattern = populate_player_pattern(size)
    play_game(size, player_pattern, game_pattern)


run_game()
