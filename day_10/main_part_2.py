import numpy as np

filename = "day_10/input"


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

    value = map[i][j]
    print(value)

    if goes_up(value):
        up_move = get_up_move(i, j, map)
        if up_move is not None:
            next_moves.append(up_move)

    if goes_down(value):
        down_move = get_down_move(i, j, map)
        if down_move is not None:
            next_moves.append(down_move)

    if goes_left(value):
        left_move = get_left_move(i, j, map)
        if left_move is not None:
            next_moves.append(left_move)

    if goes_right(value):
        right_move = get_right_move(i, j, map)
        if right_move is not None:
            next_moves.append(right_move)

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
MAP_SIZE = len(map[0, :])
print(map)

S_idx = get_starting_indexes(map)
print('S_idx', S_idx)

S_magic_letter_replacement = "F"
map[S_idx] = "F"

i, j = S_idx
is_first_move = True
position_history = [S_idx]

while True:

    possible_moves = get_next_moves(i, j, map)

    if len(possible_moves) == 0:
        raise Exception("No more moves possible")

    if len(possible_moves) != 2:
        raise Exception("lol")

    if is_first_move:
        move = possible_moves[0]  # you have to start somwhere

    else:
    
        move_set = set(possible_moves) - set(position_history)

        if len(move_set) == 1:
            move = move_set.pop()

        elif len(move_set) == 0 and S_idx in possible_moves:
            print("La boucle est bouclée")
            break
        
        else:
            raise Exception("lol")

    # Actual movement
    position_history.append(move)
    i, j = move

    is_first_move = False

steps = len(position_history)
print("steps", steps)

farthest_points = steps / 2
print("farthest_points", farthest_points)


def is_point_inside_polygon(x, y, polygon):
    """
    Check if a point (x, y) is inside a polygon defined by its vertices.
    The polygon should be a list of (x, y) vertex coordinates in a counterclockwise order.

    Reference: https://www.geeksforgeeks.org/how-to-check-if-a-given-point-lies-inside-a-polygon/
    """

    n = len(polygon)
    inside = False

    if (x, y) in polygon:
        return False

    # Count intersections of the polygon edges with a horizontal line through the test point
    count = 0
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]

        # Check if the ray crosses the edge
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
            count += 1

    # If the count is odd, the point is inside the polygon
    if count % 2 == 1:
        inside = True

    return inside


sum = 0
new_map = map
for i in range(MAP_SIZE):
    for j in range(MAP_SIZE):
        if is_point_inside_polygon(i, j, position_history):
            sum += 1
            new_map[i][j] = "X"

print(sum)
print(new_map)
