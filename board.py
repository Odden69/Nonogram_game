import math


class Board:
    """

    """
    def __init__(self, player_pattern):
        self.player_pattern = player_pattern

    size = player_pattern.len[0]

    def board_element(self, i, k, direction):
        """
        Support function for calc_header function.
        Determines the order of iteration through the board list,
        depending on header direction.
        """
        if direction == 'vertical':
            return self.game_pattern[-i][k]
        else:
            return self.game_pattern[k][-i]

    def calc_header(self, size, direction):
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
                if board_element(self, i, k, direction) == 1:
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

