import numpy as np
from collections import Counter
from functools import cmp_to_key

filename = "day_7/input_test.csv"

with open(filename, 'r') as file:
    lines = file.readlines()

# Define a mapping function
def cards_letter_to_int(element):
    mapping = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10}

    # Apply the mapping function
    return int(mapping.get(element, element))  # Use the element itself if not found in the mapping

def hand_to_list_of_int(hand):

    hand_list = list(hand)
    transformed_list = [cards_letter_to_int(item) for item in hand_list]

    return transformed_list

def get_first_score(hand):

    hand_list = list(hand)
    joker_counts = hand_list.count("X")
    # print("joker_counts", joker_counts)

    if joker_counts == 0:
        return get_score(hand)

    joker_idx = [index for index, value in enumerate(hand_list) if value == "X"]

    score = 0

    for idx in joker_idx:

        for replacement_value in ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]:
            hand_list[idx] = replacement_value
            hand_str = ''.join(hand_list)
            new_score = get_first_score(hand_str)
            score = max(score, new_score)

    return score

def get_score(hand):

    hand_list = hand_to_list_of_int(hand)

    result = Counter(hand_list)

    counts_most_common = result.most_common(1)[0][1]

    # hand score
    is_five_of_a_kind = len(set(hand_list)) == 1

    if is_five_of_a_kind:
        # print("Five of a kind")
        # score = 1000 + hand_list[0]
        return 1000

    is_four_of_a_kind = counts_most_common == 4

    if is_four_of_a_kind:
        # print("Four of a kind")
        # score = 900 + value_most_common
        return 900

    is_full_house = len(set(hand_list)) == 2 and not is_four_of_a_kind
    if is_full_house:
        # print("Full house")
        return 800

    is_three_of_a_kind = len(set(hand_list)) == 3 and counts_most_common == 3
    if is_three_of_a_kind:
        # print("Three of a kind")
        return 700

    is_two_pair = len(set(hand_list)) == 3 and not is_three_of_a_kind
    if is_two_pair:
        # print("Two pair")
        return 600

    is_one_pair = len(set(hand_list)) == 4
    if is_one_pair:
        # print("One pair")
        return 500

    is_high_card = len(set(hand_list)) == 5
    if is_high_card:
        # print("High card")
        return 400

    return 0

def get_second_score(hand):

    score = 0
    hand_list = hand_to_list_of_int(hand)
    for i, number in enumerate(hand_list):
        score += (10**(12-2*i)) * number

    return score

# Define a custom comparison function
def custom_compare(hand_x, hand_y):

    hand_x_XX= hand_x.replace("J", "X")
    hand_y_XX = hand_y.replace("J", "X")

    # Compare elements based on their custom order
    hand_x_score = get_first_score(hand_x_XX)
    hand_y_score = get_first_score(hand_y_XX)

    if hand_x_score == hand_y_score:
        hand_x_score = get_second_score(hand_x)
        hand_y_score = get_second_score(hand_y)

    return (hand_x_score > hand_y_score) - (hand_x_score < hand_y_score)


hand_str_list = []
bid_dict = {}

for id, line in enumerate(lines):
    # print("progress: ", id, "/", len(lines))
    hand_str = line.split()[0]

    bid = int(line.split()[1])
    hand_str_list.append(hand_str)
    bid_dict[hand_str] = bid

print("Sorting start")
# Sort the list based on the custom comparison function
sorted_hands = sorted(hand_str_list, key=cmp_to_key(custom_compare))
print("Sorting done")

# final stuff
sum = 0
for i, hand in enumerate(sorted_hands):

    rank = i + 1
    bid = bid_dict[hand]
    sum += bid * rank

print(sum)