import random
import math


def populate_matrix(size):
    """
    populates the board matrix with random 0s and 1s. 0 for empty and 1 for
    a filled index.
    """
    matrix = [[random.randint(0, 1) for i in range(size)] for j in range(size)]
    return matrix


# board = populate_matrix(6)
board = [[1, 0, 0, 0, 1, 1], [1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0],
         [0, 1, 0, 0, 1, 0], [1, 0, 1, 0, 1, 0], [0, 0, 1, 0, 0, 1]]


def calc_horizontal_header(size):
    header = [[0 for i in range(math.ceil(size/2))] for j in range(size)]
    i = 1
    j = 1
    k = 0
    while k < size:
        cont = False
        while i <= size:
            if board[k][-i] == 1:
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

def calc_vertical_header(size):
    header = [[0 for i in range(math.ceil(size/2))] for j in range(size)]
    i = 1
    j = 1
    k = 0
    while k < size:
        cont = False
        while i <= size:
            if board[-i][k] == 1:
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


print(board)
print(calc_horizontal_header(6))
print(calc_vertical_header(6))
