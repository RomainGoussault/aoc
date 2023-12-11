import numpy as np
from typing import List

filename = "day_11/input"


def file_2_numpy(file_path: str) -> np.ndarray:

    # Read the file and store each character in a list
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # Remove newline characters at the end of each line
        lines = [line.rstrip('\n') for line in lines]

    # Create a NumPy array from the list of characters
    array_2d = np.array([list(line) for line in lines], dtype=str)

    return array_2d


def expand_universe(map: np.ndarray):

    rows_to_expand = []
    for i in range(map.shape[0]):
        is_empty_row = set(map[i, :]) == set(".")

        if is_empty_row:
            rows_to_expand.append(i)

    columns_to_expand = []
    for j in range(map.shape[1]):
        is_empty_column = set(map[:, j]) == set(".")

        if is_empty_column:
            columns_to_expand.append(j)

    return rows_to_expand, columns_to_expand


def galexies_coordinates(map, galaxie_value) -> List[tuple]:

    indices = np.where(map == galaxie_value)
    row_index, col_index = indices
    galexies_coordinates = list(zip(row_index, col_index))

    return galexies_coordinates


def is_between(number, bound1, bound2):
    lower_bound = min(bound1, bound2)
    upper_bound = max(bound1, bound2)
    return lower_bound <= number <= upper_bound


def distance_between_galaxie(galaxie_1, galaxie_2, rows_to_expand, columns_to_expand) -> int:

    row_1, col_1 = galaxie_1
    row_2, col_2 = galaxie_2

    distance = abs(row_1 - row_2) + abs(col_1 - col_2)

    expansion = 1000000 - 1
    for rows in rows_to_expand:
        if is_between(rows, row_1, row_2):
            distance += expansion

    for column in columns_to_expand:
        if is_between(column, col_1, col_2):
            distance += expansion

    return distance


map = file_2_numpy(filename)
print("map shape", map.shape)
# print(map)
rows_to_expand, columns_to_expand = expand_universe(map)
print("map shape", map.shape)
# print(map)

galaxie_value = "#"
galexies_coordinates = galexies_coordinates(map, galaxie_value)
# print(galexies_coordinates)

sum = 0

for galaxie in galexies_coordinates:
    for galaxie_2 in galexies_coordinates:

        distance = distance_between_galaxie(galaxie, galaxie_2, rows_to_expand, columns_to_expand)
        # print(distance)
        sum += distance

print(sum/2)
