import numpy as np

filename = "day_5/input_test.csv"

try:
    with open(filename, 'r') as file:
        integers = [int(word) for word in file.read().split() if word.isdigit()]

        if integers:
            max_integer = max(integers)
            print(f"The maximum integer is: {max_integer}")
        else:
            print("No integers found in the file.")
except FileNotFoundError:
    print(f"The file {filename} was not found.")
except ValueError:
    print("The file contains non-integer values.")
except Exception as e:
    print(f"An error occurred: {e}")

MAP_SIZE = int(max_integer*1.1)


def string_to_int_list(input_string):
    # Split the string into a list of substrings
    substrings = input_string.split()

    # Convert each substring to an integer and create a list of integers
    int_list = [int(substring) for substring in substrings]

    return int_list


def get_seeds(lines):
    seed_line = lines[0]
    seeds_str = seed_line.split(":")[1]
    seeds_list = string_to_int_list(seeds_str)

    new_seeds_list = np.empty(0) # np.zeros(len(MAP_SIZE))
    for i in range(0, len(seeds_list), 2):
        print("progress seeds: " + str(int(i / len(seeds_list) /2 * 100)) + "%")
        start = seeds_list[i]
        range_seed = seeds_list[i + 1]
        new_stuff = np.arange(start, start + range_seed)
        new_seeds_list = np.concatenate((new_seeds_list, new_stuff))

    return new_seeds_list.astype(int)


def build_map(name, map_size):

    map = np.arange(map_size)

    seed_to_soil_section = False

    for line in lines:

        print("progress " + name + ": " + str(int(lines.index(line) / len(lines) * 100)) + "%")

        if name in line:
            seed_to_soil_section = True
            continue

        if seed_to_soil_section:

            if line == '\n':
                break

            destination, source, range = string_to_int_list(line)
            # print(destination, source, range)
            map[source: source + range] = np.arange(destination, destination + range)

    return map


with open(filename, 'r') as file:
    lines = file.readlines()
seeds = get_seeds(lines)
print(seeds)
print(len(seeds))


soils = []
fertilizers = []
waters = []
lights = []
temperatures = []
humiditys = []
locations = []
length = len(seeds)

seed_to_soil_map = build_map("seed-to-soil", MAP_SIZE)
for seed in seeds:
    soils.append(seed_to_soil_map[seed])
del seed_to_soil_map
del seeds

soil_to_fertilizer_map = build_map("soil-to-fertilizer", MAP_SIZE)
for soil in soils:
    fertilizers.append(soil_to_fertilizer_map[soil])
del soil_to_fertilizer_map
del soils

fertilizer_to_water = build_map("fertilizer-to-water", MAP_SIZE)
for fertilizer in fertilizers:
    waters.append(fertilizer_to_water[fertilizer])
del fertilizer_to_water
del fertilizers

water_to_light = build_map("water-to-light", MAP_SIZE)
for water in waters:
    lights.append(water_to_light[water])
del water_to_light
del waters

light_to_temperature = build_map("light-to-temperature", MAP_SIZE)
for light in lights:
    temperatures.append(light_to_temperature[light])
del light_to_temperature
del lights

temperature_to_humidity = build_map("temperature-to-humidity", MAP_SIZE)
for temperature in temperatures:
    humiditys.append(temperature_to_humidity[temperature])
del temperature_to_humidity
del temperatures

humidity_to_location = build_map("humidity-to-location", MAP_SIZE)
for humidity in humiditys:
    locations.append(humidity_to_location[humidity])
del humidity_to_location
del humiditys


print(min(locations))
