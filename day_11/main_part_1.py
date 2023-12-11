import numpy as np
from typing import List

filename = "day_11/input_test"


def file_2_numpy(file_path: str) -> np.ndarray:

    # Read the file and store each character in a list
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # Remove newline characters at the end of each line
        lines = [line.rstrip('\n') for line in lines]

    # Create a NumPy array from the list of characters
    array_2d = np.array([list(line) for line in lines], dtype=str)

    return array_2d


def expand_universe(map: np.ndarray) -> np.ndarray:

    empty_row = np.array(["." for i in range(map.shape[1])])
    new_map = map.copy()
    new_row_counter = 0
    for i in range(map.shape[0]):
        is_empty_row = set(map[i,:]) == set(".")

        if is_empty_row:
            print("Expanding universe on row", i)
            position_to_insert = i + new_row_counter
            new_map = np.insert(new_map, position_to_insert, empty_row, axis=0)
            new_row_counter += 1

    empty_column = np.array(["." for i in range(new_map.shape[0])])
    map = new_map.copy()
    new_map = map.copy()
    new_column_counter = 0

    print(map)
    for j in range(map.shape[1]):
        is_empty_column = set(map[:, j]) == set(".")

        if is_empty_column:
            print("Expanding universe on column", j)
            position_to_insert = j + new_column_counter
            new_map = np.insert(new_map, position_to_insert, empty_column, axis=1)
            new_column_counter += 1

    return new_map


def galexies_coordinates(map, galaxie_value) -> List[tuple]:

    indices = np.where(map == galaxie_value)
    row_index, col_index = indices
    galexies_coordinates = list(zip(row_index, col_index))

    return galexies_coordinates


def distance_between_galaxie(galaxie_1, galaxie_2) -> int:

    row_1, col_1 = galaxie_1
    row_2, col_2 = galaxie_2

    distance = abs(row_1 - row_2) + abs(col_1 - col_2)

    return distance


map = file_2_numpy(filename)
print("map shape", map.shape)
# print(map)
map = expand_universe(map)
print("map shape", map.shape)
# print(map)

galaxie_value = "#"
galexies_coordinates = galexies_coordinates(map, galaxie_value)
# print(galexies_coordinates)

sum = 0

for galaxie in galexies_coordinates:
    for galaxie_2 in galexies_coordinates:

        distance = distance_between_galaxie(galaxie, galaxie_2)
        # print(distance)
        sum += distance

print(sum/2)
