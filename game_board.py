"""
Prints the game board on the terminal
"""
from math import ceil
import game_entry


def board_element(i, k, direction, game_pattern):
    """
    Support function for calc_header function.
    Determines the order of iteration through the board list,
    depending on header direction.
    """
    if direction == 'vertical':
        return game_pattern[-i][k]
    else:
        return game_pattern[k][-i]


def calc_header(size, direction, game_pattern):
    """
    Calculates a header as a list of lists from values in the game_pattern.
    """
    header = [[0 for i in range(ceil(size/2))] for j in range(size)]
    i = 1
    j = 1
    k = 0
    while k < size:
        cont = False
        while i <= size:
            if board_element(i, k, direction, game_pattern) == '1':
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


def print_vert_header(size, game_pattern):
    """
    Converts the vertical header list to a string
    """
    string = ''
    i = 0
    while i < len(calc_header(size, 'vertical', game_pattern)[0]):
        string = string + calc_margin(size)
        for header_list in calc_header(size, 'vertical', game_pattern):
            string_part = header_integer_to_string(header_list[i])
            string = string + string_part + ' '
        string = string + '\n'
        i += 1
    string = string[0:-2]
    return string


def print_horiz_header_row(size, i, game_pattern):
    """
    Converts a list of the horizontal header list to a string
    """
    string = ' '
    for header in calc_header(size, 'horizontal', game_pattern)[i]:
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


def print_game_board(size, player_pattern, game_pattern):
    """
    Prints the game board
    """
    print(print_vert_header(size, game_pattern))
    i = 0
    j = 1
    string = ''
    while i < size:
        print(print_horiz_header_row(size, i, game_pattern) +
              print_board_row_from_players_pattern(size, i, player_pattern) +
              game_entry.available_rows[i])
        i += 1
    while j <= size:
        string = string + str(j) + ' '
        j += 1
    print(calc_margin(size) + string)
