import numpy as np

filename = "day_6/input_test.csv"


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

time = int(lines[0].replace("Time:", "").replace(" ", ""))
best_distance_recorded = int(lines[1].replace("Distance:", "").replace(" ", ""))
print(time)
print(best_distance_recorded)

sum = 0

for hold_time in range(0, time+1):
    distance_traveled = get_distance_traveled(hold_time, time)
    # print(distance_traveled)

    win = distance_traveled > best_distance_recorded
    if win:
        sum = sum + 1

print(sum)