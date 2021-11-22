import random


def populate_matrix(size):
    """
    populates the board matrix with random 0s and 1s. 0 for empty and 1 for
    a filled index.
    """
    matrix = [[random.randint(0, 1) for i in range(size)] for i in range(size)]
    return matrix
