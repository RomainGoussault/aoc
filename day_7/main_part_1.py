from collections import Counter
from functools import cmp_to_key

filename = "input_test.csv"

with open(filename, 'r') as file:
    lines = file.readlines()


# Define a mapping function
def transform_element(element):
    mapping = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}

    # Apply the mapping function
    return int(mapping.get(element, element))  # Use the element itself if not found in the mapping

def hand_to_list_of_int(hand):

    hand_list = list(hand)
    transformed_list = [transform_element(item) for item in hand_list]

    return transformed_list

def get_score(hand):

    hand_list = hand_to_list_of_int(hand)

    result = Counter(hand_list)

    counts_most_common = result.most_common(1)[0][1]
    value_most_common = result.most_common(1)[0][0]

    # print("counts_most_common", counts_most_common)
    # print("value_most_common", value_most_common)

    # hand score
    is_five_of_a_kind = len(set(hand_list)) == 1

    if is_five_of_a_kind:
        # print("Five of a kind")
        # score = 1000 + hand_list[0]
        return 1000

    counts_second_most_common = result.most_common(2)[1][1]
    # print("counts_second_most_common", counts_most_common)

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

    # Compare elements based on their custom order
    hand_x_score = get_score(hand_x)
    hand_y_score = get_score(hand_y)

    if hand_x_score == hand_y_score:
        hand_x_score = get_second_score(hand_x)
        hand_y_score = get_second_score(hand_y)

    return (hand_x_score > hand_y_score) - (hand_x_score < hand_y_score)


hand_str_list = []
dict_machine = {}

for id, line in enumerate(lines):
    hand_str = line.split()[0]
    bid = int(line.split()[1])
    # print(hand_str, bid)
    hand_str_list.append(hand_str)
    dict_machine[hand_str] = bid

# Sort the list based on the custom comparison function
sorted_hands = sorted(hand_str_list, key=cmp_to_key(custom_compare))
# print(sorted_hands)


# final stuff
sum = 0
for i, hand in enumerate(sorted_hands):

    rank = i + 1
    bid = dict_machine[hand]
    sum += bid * rank

print(sum)