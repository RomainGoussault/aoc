import re

filename = "input.csv"

MAX_CUBES = {"red":12, "green":13, "blue":14}

def get_cubes_count_dict(tirage):
    cubes_list = tirage.split(",")

    cubes_count_dict = {}
    for cubes in cubes_list:
        cubes_count = int(re.findall(r'\d+',cubes)[0])
        color = re.sub(r'[\d\s]+', '', cubes)
        cubes_count_dict[color] = cubes_count
        
    return cubes_count_dict
    
def power_of_game(line):

    line = line.split(":")[1]
    tirages = line.split(";")

    max_cube_count_dict = {"blue":0, "red":0, "green":0 }

    for tirage in tirages:

        cubes_count_dict = get_cubes_count_dict(tirage)

        for color, color_count in cubes_count_dict.items():

            if color_count > max_cube_count_dict[color]:
                max_cube_count_dict[color] = color_count

    # get power
    power = max(1, max_cube_count_dict["blue"]) * max(1, max_cube_count_dict["red"]) * max(1, max_cube_count_dict["green"])
    
    return power

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

    power = power_of_game(line)
    print("power", power)

    sum = sum + power

print(sum)

