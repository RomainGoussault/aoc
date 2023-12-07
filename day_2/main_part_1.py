import re

filename = "input.csv"

MAX_CUBES = {"red":12, "green":13, "blue":14}

def is_tirage_possible(tirage):
    cubes_list = tirage.split(",")

    for cubes in cubes_list:
        cubes_count = int(re.findall(r'\d+',cubes)[0])
        color = re.sub(r'[\d\s]+', '', cubes)
        max_allowed_cubes = MAX_CUBES[color]
        is_tirage_possible = cubes_count <= max_allowed_cubes
        
        if not is_tirage_possible:
            return False
    
    return True
    
def is_game_possible_func(line):

    line = line.split(":")[1]
    tirages = line.split(";")

    for tirage in tirages:

        if not is_tirage_possible(tirage):
            return False

    return True

def get_first_number(input_string):
    # Use regular expression to find the first number
    match = re.search(r'\d+', input_string)
    
    # Check if a match is found
    if match:
        # Return the matched number as an integer
        return int(match.group())
    else:
        # Return None if no number is found
        return None
    

with open(filename) as file:
    lines = [line.rstrip() for line in file]

sum = 0

for line in lines:

    id = get_first_number(line)

    print('')
    print("Game ID", id)

    is_game_possible = is_game_possible_func(line)
    # print("is_game_possible", is_game_possible)

    if is_game_possible:
        sum = sum + int(id)

print(sum)

