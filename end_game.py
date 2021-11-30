"""
Contains functions to give the player options at the end of the game
"""


def quit_game(size, game_pattern):
    """
    Prints an options message at the end of a game
    """
    message = '''Thank you for playing the Nonogram game!\n
        Choose one the following options by typing the number.\n
        1. Back to the start menu.\n
        2. Play the same game again. \n'''
    print(message)
    players_choice_end_menu(size, game_pattern)


def players_choice_end_menu(size, game_pattern):
    while True:
        try:
            choice = int(input('Make your choice: '))
        except ValueError:
            print('        That was not a number. Please try again.')
        else:
            if choice == 1:
                from run import run_game
                run_game()
            elif choice == 2:
                from run import restart_game
                restart_game(size, game_pattern)
            else:
                print('       That was not a valid choice, please type 1 or 2')
