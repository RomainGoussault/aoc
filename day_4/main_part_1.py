import re

filename = "day_4/input.csv"

def string_to_int_list(input_string):
    # Split the string into a list of substrings
    substrings = input_string.split()

    # Convert each substring to an integer and create a list of integers
    int_list = [int(substring) for substring in substrings]

    return int_list

def line_to_two_int_list(line):
    # print(line)

    line_split = line.split(':')
    numbers = line_split[1]

    numbers_split = numbers.split("|")
    winning_numbers_str = numbers_split[0]
    numbers_str = numbers_split[1]

    numbers = string_to_int_list(numbers_str)
    winning_numbers_str = string_to_int_list(winning_numbers_str)

    return numbers, winning_numbers_str

def points_from_two_int_list(numbers, winning_numbers_str):

    intersection = set(numbers).intersection(set(winning_numbers_str))
    number_of_winning_numbers = len(intersection)

    points = int(2**(number_of_winning_numbers-1))

    return points

with open(filename, 'r') as file:
    lines = file.readlines()

sum = 0
for line in lines:
    line = line.strip()
    numbers, winning_numbers_str = line_to_two_int_list(line)
    points = points_from_two_int_list(numbers, winning_numbers_str)

    sum += points

print(sum)