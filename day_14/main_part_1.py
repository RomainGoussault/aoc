import numpy as np

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


def can_go_up(map, i, j):
    if i == 0:
        return False

    return map[i - 1, j] == "."


def move_rock(map, i, j, steps):
    map[i, j] = "."
    assert map[i - steps, j] == "."
    map[i - steps, j] = "O"


map = file_2_numpy(filename)
print("map shape", map.shape)
print(map)

number_of_lines = map.shape[0]
number_of_columns = map.shape[1]

for i in range(number_of_lines):
    for j in range(number_of_columns):

        is_rounded_rock = map[i, j] == "O"
        if not is_rounded_rock:
            continue

        steps = 0
        while can_go_up(map, i-steps, j):
            steps += 1

        move_rock(map, i, j, steps)

print("After moving rocks")
print(map)

# Counting
sum = 0
for i in range(number_of_lines):
    load_factor = number_of_lines - i
    number_of_rounded_rocks = np.sum(map[i, :] == "O")
    sum += load_factor * number_of_rounded_rocks

print(sum)
