import numpy as np


def file_2_numpy(file_path):
    # Specify the file path
    file_path = 'input.csv'  # Replace with the actual path to your file

    # Read the file and store each character in a list
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # Remove newline characters at the end of each line
        lines = [line.rstrip('\n') for line in lines]

    # Create a NumPy array from the list of characters
    array_2d = np.array([list(line) for line in lines], dtype=str)

    return array_2d


def get_neighbor_digit_coordinates(array, row, col):
    neighbors = []
    rows, cols = len(array), len(array[0])

    for i in range(max(0, row - 1), min(row + 2, rows)):
        for j in range(max(0, col - 1), min(col + 2, cols)):
            if i != row or j != col:

                value = array[i][j]
                if value.isdigit():
                    coordinates = (i,j)
                    neighbors.append(coordinates)

    return neighbors

def get_first_digit_of_adjacent_part(array, i, j):

    digit_coordinates_list = get_neighbor_digit_coordinates(array, i, j)
    first_digit_coordinates_set = set()

    for digit_coordinates in digit_coordinates_list:
                
        # find start of number
        first_digit_coord = digit_coordinates
        i = first_digit_coord[0]
        j = first_digit_coord[1]

        while array_2d[i][j-1].isdigit():
            j = j - 1
            first_digit_coord = (i, j)

            if j == 0:
                break
        
        first_digit_coordinates_set.add(first_digit_coord)

    print(first_digit_coordinates_set)

    return first_digit_coordinates_set
    

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


array_2d = file_2_numpy('input_test.csv')
rows, cols = array_2d.shape
sum = 0
print(array_2d.shape)
print(array_2d)
target_list = []

for i in range(rows):
    for j in range(cols):

        is_a_gear = array_2d[i][j] == '*'
        
        if is_a_gear:
            
            first_digit_coordinates_set = get_first_digit_of_adjacent_part(array_2d, i, j)
            if(len(first_digit_coordinates_set)) == 2:

                print("")
                print("GEAR RATIO FOUND")
                print(i, j)

                mul = 1 
                for coord in first_digit_coordinates_set:
                    
                    digits_count = get_digits_counts(array_2d, coord[0], coord[1])
                    print(digits_count)

                    number_coordinates = [k for k in range(coord[1], coord[1]+digits_count)]
                    char_list = array_2d[coord[0], number_coordinates]
                    result_number = int(''.join(char_list))
                    mul = mul * result_number
            
                print("mul", mul)
                sum = sum + mul

print(sum)
