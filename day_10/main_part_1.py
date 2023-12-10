import numpy as np

filename = "day_10/input_test.csv"


def file_2_numpy(file_path):

    # Read the file and store each character in a list
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # Remove newline characters at the end of each line
        lines = [line.rstrip('\n') for line in lines]

    # Create a NumPy array from the list of characters
    array_2d = np.array([list(line) for line in lines], dtype=str)

    return array_2d


def get_starting_indexes(map) -> tuple:

    S_idx = np.where(map == "S")
    S_i = S_idx[0][0]
    S_j = S_idx[1][0]

    return (S_i, S_j)


def get_next_moves(i, j, map):

    next_moves = []

    rows, cols = map.shape

    value = map[i][j]
    print(value)

    if value == "L":

        up_move = get_up_move(i, j, map)
        if up_move is not None:
            next_moves.append(up_move)

        if is_right_move_possible(i, j, map):
            print("Going right")
            next_moves.append((i-1, j))
        else:
            print("can't go right")
        
    return next_moves


def get_up_move(i, j, map):

    if is_up_move_possible(i, j, map):
        return (i-1, j)
    else:
        return None


def get_down_move(i, j, map):

    if is_down_move_possible(i, j, map):
        return (i+1, j)
    else:
        return None


def get_right_move(i, j, map):

    if is_right_move_possible(i, j, map):
        return (i, j+1)
    else:
        return None


def get_left_move(i, j, map):

    if is_left_move_possible(i, j, map):
        return (i, j-1)
    else:
        return None


def goes_up(value) -> bool:
    return value in ['|', 'L', 'J']


def goes_down(value) -> bool:
    return value in ['|', '7', 'F']


def goes_left(value) -> bool:
    return value in ['-', '7', 'J']


def goes_right(value) -> bool:
    return value in ['-', 'L', 'F']


def is_up_move_possible(i, j, map):

    if i == 0:
        return False

    value_up = map[i-1][j]

    if goes_down(value_up):
        return True
    else:
        return False


def is_down_move_possible(i, j, map):

    if i == len(map[0, :])-1:
        return False

    value_down = map[i+1][j]

    if goes_up(value_down):
        return True
    else:
        return False


def is_left_move_possible(i, j, map):

    if j == 0:
        return False

    value_left = map[i][j-1]

    if goes_right(value_left):
        return True
    else:
        return False


def is_right_move_possible(i, j, map):

    if j == len(map[0, :])-1:
        return False

    value_right = map[i][j+1]

    if goes_left(value_right):
        return True
    else:
        return False


map = file_2_numpy(filename)
print("map shape", map.shape)
print(map)

S_idx = get_starting_indexes(map)
print('S_idx', S_idx)

# find connected to S
moves = get_next_moves(3, 1, map)

