import random
import math
import game_entry

player_pattern = []


def print_start_menu():
    message = '''Welcome to the Nonogram game!\n
        Choose one the following options by typing the number.\n
        1. How to play.\n
        2. Play Game\n'''
    print(message)


def players_choice_start_menu():
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
    print('        This is how to play')
    input('Enter any key to go back to main menu: ')
    print_start_menu()


def populate_game_pattern(size):
    """
    populates the game board matrix with random 0s and 1s.
    0 for empty and 1 for a filled index.
    """
    game_pattern = [[random.randint(0, 1) for i in range(size)]
                    for j in range(size)]
    return game_pattern


def populate_player_pattern(size):
    """
    populates the players board matrix with a single dot for each index.
    """
    player_pattern = [[chr(183) for i in range(size)] for j in range(size)]
    return player_pattern


player_pattern = populate_player_pattern(6)

board = populate_game_pattern(6)
'''
board = [[1, 0, 1, 0, 1, 1], [0, 0, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0],
         [1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [1, 0, 1, 0, 0, 1]]        

board = [[0, 1, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [1, 1, 0, 1, 1, 0],
         [1, 1, 1, 1, 0, 1], [1, 0, 0, 1, 1, 1], [1, 1, 0, 1, 0, 1]]
'''


def board_element(i, k, direction, board):
    """
    Support function for calc_header function.
    Determines the order of iteration through the board list,
    depending on header direction.
    """
    if direction == 'vertical':
        return board[-i][k]
    else:
        return board[k][-i]


def calc_header(size, direction, board):
    """
    Calculates a header as a list of lists from values in the board list.
    """
    header = [[0 for i in range(math.ceil(size/2))] for j in range(size)]
    i = 1
    j = 1
    k = 0
    while k < size:
        cont = False
        while i <= size:
            if board_element(i, k, direction, board) == 1:
                cont = True
                header[k][-j] += 1
                i += 1
            elif cont:
                j += 1
                i += 1
                cont = False
            else:
                i += 1
        k += 1
        i = 1
        j = 1
    return header


def calc_margin(size):
    """
    Returns a string of spaces depending on board size.
    Gives the space to the right of the vertical header.
    """
    margin_string = ' ' * (size + 1)
    return margin_string


def header_integer_to_string(integer):
    """
    Converts the elements in the header list to a string depending on value.
    """
    if integer == 0:
        string = ' '
    else:
        string = str(integer)
    return string


def print_vert_header(size, board):
    """
    Converts the vertical header list to a string
    """
    string = ''
    i = 0
    while i < len(calc_header(size, 'vertical', board)[0]):
        string = string + calc_margin(size)
        for header_list in calc_header(size, 'vertical', board):
            string_part = header_integer_to_string(header_list[i])
            string = string + string_part + ' '
        string = string + '\n'
        i += 1
    string = string[0:-2]
    return string


def print_horiz_header_row(size, i, board):
    """
    Converts a list of the horizontal header list to a string
    """
    string = ' '
    for header in calc_header(size, 'horizontal', board)[i]:
        string_part = header_integer_to_string(header)
        string = string + string_part + ' '
    return string


def print_board_row_from_players_pattern(size, i, player_pattern):
    """
    Gives a string of the players pattern for each row of the board
    """
    string = ''
    k = 0
    while k < size:
        string_part = player_pattern[i][k]
        string = string + string_part + ' '
        k += 1
    return string


def print_game_board(size, player_pattern, board):
    """
    Prints the game board
    """
    print(print_vert_header(size, board))
    i = 0
    j = 1
    string = ''
    while i < size:
        print(print_horiz_header_row(size, i, board) +
              print_board_row_from_players_pattern(size, i, player_pattern) +
              game_entry.available_rows[i])
        i += 1
    while j <= size:
        string = string + str(j) + ' '
        j += 1
    print(calc_margin(size) + string)
