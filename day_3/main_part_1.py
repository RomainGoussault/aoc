import numpy as np


def file_2_numpy(file_path):
    # Specify the file path
    file_path = 'day_3/input.csv'  # Replace with the actual path to your file

    # Read the file and store each character in a list
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # Remove newline characters at the end of each line
        lines = [line.rstrip('\n') for line in lines]

    # Create a NumPy array from the list of characters
    array_2d = np.array([list(line) for line in lines], dtype=str)

    return array_2d

array_2d = file_2_numpy('input_test.csv')
rows, cols = array_2d.shape

print(array_2d.shape)

# print(array_2d)

def get_8_neighbors(array, row, col):
    neighbors = []
    rows, cols = len(array), len(array[0])

    for i in range(max(0, row - 1), min(row + 2, rows)):
        for j in range(max(0, col - 1), min(col + 2, cols)):
            if i != row or j != col:
                neighbors.append(array[i][j])

    return neighbors

def is_symbol_close_by(array, row, col):

    neighbors = get_8_neighbors(array, row, col)
    number_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    symbol_set = (set(neighbors) - number_set) - {'.'}
    
    is_symbol_close_by = len(symbol_set) > 0

    return is_symbol_close_by

def get_digits_counts(array_2d, i, j):

    rows_len, cols_len = len(array_2d), len(array_2d[0])

    digits_counts = 1

    if j == rows_len-1:
        return digits_counts
    
    while array_2d[i][j+1].isdigit():
        digits_counts = digits_counts+1
        j = j + 1
        if j == rows_len-1:
            return digits_counts

    return digits_counts



target_list = []

for i in range(rows):
    j = 0
    while j  <cols:

        is_a_digit = array_2d[i][j].isdigit()
        
        if is_a_digit:

            # print()
            # print(i, j)
            digits_count = get_digits_counts(array_2d, i, j)
            # print("digits_count", digits_count)

            number_coordinates = [k for k in range(j, j+digits_count)]

            # print("number_coordinates", number_coordinates)
            symbol_found = False
            for k in number_coordinates:

                if is_symbol_close_by(array_2d, i, k):
                    symbol_found = True
            
            j =  j+digits_count
            if symbol_found:

                # No symbol close by!!
                print()
                print(i)
                print(number_coordinates)
                print("NOT PART")
                char_list = array_2d[i, number_coordinates]
                print(char_list)
                result_number = int(''.join(char_list))
                target_list.append(result_number)
                
        else:
            j=j+1
            

print(target_list)
sum = 0
for k in target_list:
    sum = sum + k

print(sum)