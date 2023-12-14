import numpy as np
import time
# import sys

filename = "day_14/input"


def file_2_numpy(file_path: str) -> np.ndarray:

    # Read the file and store each character in a list
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # Remove newline characters at the end of each line
        lines = [line.rstrip('\n') for line in lines]

    # Create a NumPy array from the list of characters
    array_2d = np.array([list(line) for line in lines], dtype=str)

    return array_2d


def can_move(map, i, j, direction, steps):

    if direction == "north":
        target_line = i - steps - 1
        if target_line < 0:
            return False

        return map[target_line, j] == "."

    elif direction == "west":
        target_column = j - steps - 1
        if target_column < 0:
            return False

        return map[i, target_column] == "."

    elif direction == "south":
        target_line = i + steps + 1
        if target_line >= map.shape[0]:
            return False

        return map[target_line, j] == "."

    elif direction == "east":
        target_column = j + steps + 1
        if target_column >= map.shape[1]:
            return False

        return map[i, target_column] == "."
    else:
        raise Exception("Direction not recognized")


def move_rock(map, i, j, direction, steps):

    if direction == "north":
        map[i, j] = "."
        map[i - steps, j] = "O"
    elif direction == "west":
        map[i, j] = "."
        map[i, j - steps] = "O"
    elif direction == "south":
        map[i, j] = "."
        map[i + steps, j] = "O"
    elif direction == "east":
        map[i, j] = "."
        map[i, j + steps] = "O"
    else:
        raise Exception("Direction not recognized")

    return map


map = file_2_numpy(filename)
print("map shape", map.shape)
print(map)

number_of_lines = map.shape[0]
number_of_columns = map.shape[1]

start_time = time.time()

direction_list = ["north", "west", "south", "east"]
total_iterations = 1000000000
target_index = total_iterations
start_index = 141
cycle_length = 38
relative_index = start_index + (target_index - start_index) % cycle_length
print("relative index", relative_index)
map_list = []


for k in range(relative_index):

    # check if cycle
    for i, map2 in enumerate(map_list):
        if np.array_equal(map, map2):
            print("Cycle detected, cycle length", k-i)
            print("Cycle detected at iteration", k)
            cycle_length = k
            # sys.exit()

    map_list.append(map.copy())

    for direction in direction_list:

        row_index, col_index = np.where(map == "O")
        rounded_rocks_idx_list = list(zip(row_index, col_index))

        if direction == "south" or direction == "east":
            rounded_rocks_idx_list.reverse()

        # print(direction)
        for rounded_rocks_idx in rounded_rocks_idx_list:
            (i, j) = rounded_rocks_idx

            steps = 0
            while can_move(map, i, j, direction, steps):
                steps += 1

            map = move_rock(map, i, j, direction, steps)

    # Print progress
    if k % 10000 == 0 and k != 0:
        elapsed_time = time.time() - start_time
        iterations_per_second = k / elapsed_time
        remaining_iterations = total_iterations - k
        remaining_time_hours = remaining_iterations / iterations_per_second / 3600

        print(f"Progress: {i}/{total_iterations}, "
              f"Elapsed Time: {elapsed_time:.2f}s, "
              f"Remaining Time: {remaining_time_hours:.2f}h")


# Counting
print("Counting")
sum = 0
for i in range(number_of_lines):
    load_factor = number_of_lines - i
    number_of_rounded_rocks = np.sum(map[i, :] == "O")
    sum += load_factor * number_of_rounded_rocks

print(sum)
