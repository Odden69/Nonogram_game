"""
Contains functions to give the player options at the end of the game
"""
from clear_screen import clear_screen


def quit_game(size, player_pattern, game_pattern):
    """
    Prints an options message at the end of a game
    """
    clear_screen()
    message = '''Thank you for playing the Nonogram game!\n
        Choose one the following options by typing the number.\n
        1. Back to the start menu.\n
        2. Play the same game again. \n'''
    print(message)
    players_choice_end_menu(size, game_pattern)


def players_choice_end_menu(size, game_pattern):
    """
    Gets the players choice after finishing a game
    """
    while True:
        try:
            choice = int(input('Make your choice: '))
        except ValueError:
            print('        That was not a number. Please try again.')
        else:
            if choice == 1:
                from run_game import run_game
                run_game()
            elif choice == 2:
                from run_game import restart_game
                restart_game(size, game_pattern)
            else:
                print('       That was not a valid choice, please type 1 or 2')
