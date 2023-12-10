import numpy as np

filename = "day_9/input_test.csv"


def string_to_int_list(input_string):
    # Split the string into a list of substrings
    substrings = input_string.split()

    # Convert each substring to an integer and create a list of integers
    int_list = [int(substring) for substring in substrings]

    return int_list
    

def is_all_zero(line):
    for i in range(len(line)):
        if line[i] != 0 and not np.isnan(line[i]):
            return False
    return True


with open(filename) as file:
    lines = [line.rstrip() for line in file]

sum = 0

for line in lines:

    history = string_to_int_list(line)
    history_length = len(history)

    array_2d = np.full((history_length+1, history_length+1), 0)
    array_2d[0, :-1] = history

    all_zeros_line_index = 0
    # fill array_2d
    for i in range(1, history_length-1):
        for j in range(history_length-i):
            array_2d[i, j] = array_2d[i-1, j+1] - array_2d[i-1, j]

        if is_all_zero(array_2d[i, :]):
            # print("All zeros found at row: ", i)
            all_zeros_line_index = i
            break

    column_to_fill = len(array_2d) - 1 - all_zeros_line_index
    j = column_to_fill

    for i in range(all_zeros_line_index, -1, -1):
        array_2d[i, j] = array_2d[i, j-1] + array_2d[i+1, j-1]
        j = j + 1

    sum += array_2d[0, -1]

print(sum)