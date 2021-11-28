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


def finish_game():
    print('GAME FINISHED')


def update_player_pattern(new_coord, new_symbol, size):
    row = available_rows.index(new_coord[0])
    column = int(new_coord[1])-1
    player_pattern[row][column] = new_symbol
    print(player_pattern)
    checklist = [chr(183) in list for list in player_pattern]
    if any(checklist):
        get_board_input_from_player(size)
        return
    else:
        print('You have filled the board, the game is finished')
        finish_game()
        return


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
                  'Enter the coordinate in the form of one letter and one '
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
    while True:
        try:
            second_entry = input('Do you want the coordinate to be empty '
                                 'or filled? \n'
                                 'Enter an E for empty or an F for filled: ')
            new_symbol = second_entry.upper()
            if new_symbol == 'Q':
                quit_game()
                return
            elif not new_symbol == 'E' and not new_symbol == 'F':
                raise Exception
        except Exception:
            print(f'"{second_entry}" is not a valid entry. Please try again')
        else:
            break
    if new_symbol == 'E':
        new_symbol = chr(0x2BBD)
    else:
        new_symbol = chr(0x25A0)
    update_player_pattern(new_coord, new_symbol, size)


get_board_input_from_player(6)
