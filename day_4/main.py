import re
import numpy as np

filename = "day_4/input.csv"


def extract_numbers(string):
    return re.findall(r'\d+', string)


def OOOOOLD(game_id, numbers, winning_numbers_str, lines):

    score = 0
    intersection = set(numbers).intersection(set(winning_numbers_str))

    if len(intersection) == 0:
        return 1

    g = game_id
    for number in intersection:
        g = game_id + 1
        gg, numbers, winning_numbers_str = line_to_two_int_list(lines[g-1])
        score = 0 + score + get_matching_cards(g, numbers, winning_numbers_str, lines)

    return score


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
    game_id = int(extract_numbers(line_split[0])[0])

    numbers_split = numbers.split("|")
    winning_numbers_str = numbers_split[0]
    numbers_str = numbers_split[1]

    numbers = string_to_int_list(numbers_str)
    winning_numbers_str = string_to_int_list(winning_numbers_str)

    return game_id, numbers, winning_numbers_str


def points_from_two_int_list(numbers, winning_numbers_str):

    intersection = set(numbers).intersection(set(winning_numbers_str))
    number_of_winning_numbers = len(intersection)

    points = int(2**(number_of_winning_numbers-1))

    return points


with open(filename, 'r') as file:
    lines = file.readlines()


def get_matching_cards(game_id, numbers, winning_numbers_str, cards_list):

    intersection = set(numbers).intersection(set(winning_numbers_str))

    if len(intersection) == 0:
        return cards_list

    g = game_id
    for number in intersection:
        g = g + 1
        cards_list[g-1] += 1 * cards_list[game_id-1]

    return cards_list


number_of_scratchcards = 0
cards_list = np.ones(len(lines))

for line in lines:
    line = line.strip()
    game_id, numbers, winning_numbers_str = line_to_two_int_list(line)

    print("game_id: ", game_id)

    cards_list = get_matching_cards(game_id, numbers, winning_numbers_str, cards_list)
    print(cards_list)

print(cards_list)
print(np.sum(cards_list))
