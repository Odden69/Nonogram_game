import random
import math


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


board = populate_game_pattern(6)
'''
board = [[1, 0, 1, 0, 1, 1], [0, 0, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0],
         [1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [1, 0, 1, 0, 0, 1]]

board = [[0, 1, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [1, 1, 0, 1, 1, 0],
         [1, 1, 1, 1, 0, 1], [1, 0, 0, 1, 1, 1], [1, 1, 0, 1, 0, 1]]
'''


def board_element(i, k, direction):
    """
    Support function for calc_header function.
    Determines the order of iteration through the board list,
    depending on header direction.
    """
    if direction == 'vertical':
        return board[-i][k]
    else:
        return board[k][-i]


def calc_header(size, direction):
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
            if board_element(i, k, direction) == 1:
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


def print_vert_header(size):
    """
    Converts the vertical header list to a string
    """
    string = ''
    i = 0
    while i < len(calc_header(size, 'vertical')[0]):
        string = string + calc_margin(size)
        for header_list in calc_header(size, 'vertical'):
            string_part = header_integer_to_string(header_list[i])
            string = string + string_part + ' '
        string = string + '\n'
        i += 1
    string = string[0:-2]
    return string


def print_horiz_header_row(size, i):
    """
    Converts a list of the horizontal header list to a string
    """
    string = ' '
    for header in calc_header(size, 'horizontal')[i]:
        string_part = header_integer_to_string(header)
        string = string + string_part + ' '
    return string


def print_empty_game_board_row(size):
    """
    Fills the empty game board with dots
    """
    string = ''
    i = 0
    while i < size:
        string_part = chr(183)
        string = string + string_part + ' '
        i += 1
    return string


def print_game_board(size):
    """
    Prints the game board
    """
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O']
    print(print_vert_header(size))
    i = 0
    j = 1
    string = ''
    while i < size:
        print(print_horiz_header_row(size, i) +
              print_empty_game_board_row(size) + letters[i])
        i += 1
    while j <= size:
        string = string + str(j) + ' '
        j += 1
    print(calc_margin(size) + string)


print_game_board(6)
print(board)
