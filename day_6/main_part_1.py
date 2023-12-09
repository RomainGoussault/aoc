import numpy as np

filename = "day_6/input.csv"


def string_to_int_list(input_string):
    # Split the string into a list of substrings
    substrings = input_string.split()

    # Convert each substring to an integer and create a list of integers
    int_list = [int(substring) for substring in substrings]

    return int_list


with open(filename, 'r') as file:
    lines = file.readlines()


def get_distance_traveled(hold_time, time):

    speed = hold_time
    time_left = time - hold_time
    distance = speed * time_left

    return distance

times = string_to_int_list(lines[0].replace("Time:", ""))
best_distances_reccorded = string_to_int_list(lines[1].replace("Distance:", ""))
print(times)
print(best_distances_reccorded)

number_of_wins = np.zeros(len(times))
i = 0
for time, best_distance_reccorded in zip(times, best_distances_reccorded):

    for hold_time in range(0, time+1):
        distance_traveled = get_distance_traveled(hold_time, time)
        print(distance_traveled)

        win = distance_traveled > best_distance_reccorded

        if win:
            number_of_wins[i] = number_of_wins[i] + 1

    i = i + 1

mul = 1
for wins in number_of_wins:
    mul = mul * wins
print(mul)