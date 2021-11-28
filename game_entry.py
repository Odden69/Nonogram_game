available_rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O']
player_pattern = []


def populate_player_pattern(size):
    """
    populates the players board matrix with a single dot for each index.
    """
    player_pattern = [[chr(183) for i in range(size)] for j in range(size)]
    return player_pattern


player_pattern = populate_player_pattern(6)


def get_valid_coordinates(size):
    valid_coordinates = []
    i = 0
    j = 0
    while j < size:
        while i < size:
            valid_coordinate = f'{available_rows[j]}{i+1}'
            valid_coordinates.append(valid_coordinate)
            i += 1
        j += 1
        i = 0
    return valid_coordinates


def quit_game():
    print('QUIT GAME')


def update_player_pattern(new_coord):
    print(new_coord)


def get_board_input_from_player(size):
    while True:
        try:
            first_entry = input('Enter the coordinate of your choice '
                                '(e.g. A2): ')
            new_coord = first_entry.upper()
            if new_coord == 'Q':
                quit_game()
                return
            elif len(new_coord) != 2:
                raise Exception
            elif not new_coord[0].isalpha() or not new_coord[1].isdigit():
                raise Exception
        except Exception:
            print(f'"{first_entry}" is not a valid entry. \n'
                  'The coordinate needs to be in the form of one letter and one '
                  'number (e.g. A2).')
        else:
            try:
                if new_coord not in get_valid_coordinates(size):
                    raise Exception
            except Exception:
                print('The coordinate you entered is outside the board. \n'
                      'Please try again.')
            else:
                break
    update_player_pattern(new_coord)


get_board_input_from_player(6)
