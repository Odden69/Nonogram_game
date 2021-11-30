import compare

available_rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                  'M', 'N', 'O']


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


def update_player_pattern(size, new_coord, new_symbol, player_pattern,
                          game_pattern):
    row = available_rows.index(new_coord[0])
    column = int(new_coord[1])-1
    player_pattern[row][column] = new_symbol
    checklist = [chr(183) in list for list in player_pattern]
    if any(checklist):
        return player_pattern
    else:
        print('You have filled the board, the game is finished\n')
        compare.compare_patterns(size, player_pattern, game_pattern)
        return


def get_board_input_from_player(size, player_pattern, game_pattern):
    while True:
        try:
            first_entry = input('Enter the coordinate of your choice '
                                '(e.g. A2): ')
            new_coord = first_entry.upper()
            if new_coord == 'Q':
                quit_game()
                return
            elif new_coord == 'X':
                compare.compare_patterns(size, player_pattern, game_pattern)
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
            elif new_symbol == 'X':
                compare.compare_patterns(size, player_pattern, game_pattern)
            elif not new_symbol == 'E' and not new_symbol == 'F':
                raise Exception
        except Exception:
            print(f'"{second_entry}" is not a valid entry. Please try again')
        else:
            break
    if new_symbol == 'E':
        new_symbol = chr(0x25A1)
    else:
        new_symbol = chr(0x25A0)
    update_player_pattern(size, new_coord, new_symbol, player_pattern,
                          game_pattern)
    return player_pattern
