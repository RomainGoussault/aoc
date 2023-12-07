import re
import pandas as pd

df  = pd.read_csv("input.csv", header=None)

candidates = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def str_2_digit(input):
    output = input.replace("one", "1")
    output = output.replace("two", "2")
    output = output.replace("three", "3")
    output = output.replace("four", "4")
    output = output.replace("five", "5")
    output = output.replace("six", "6")
    output = output.replace("seven", "7")
    output = output.replace("eight", "8")
    output = output.replace("nine", "9")
    return output

def find_idx(input, substring):
    return [m.start() for m in re.finditer(substring, input)]

def get_z(input_str):

    lower_index = 100000
    upper_index = -1
    first_digit = ""
    last_digit = ""

    for candidate in candidates:
        # print("candidate", candidate)
        try:
            indexes = find_idx(input_str, candidate)
            print(indexes)

            for index in indexes:
                # print("index", index)
                if index < lower_index:
                    # print("update first digit")
                    first_digit = candidate
                    lower_index = index

                if index > upper_index:
                    # print("update last digit")
                    last_digit = candidate
                    upper_index = index

        except:
            a = 3

    first_num = str_2_digit(first_digit)
    last_num = str_2_digit(last_digit)

    z = int(first_num + last_num)
    return z

sum = 0
for index, row in df.iterrows():

    input_str = row[0]
    z = get_z(input_str)

    print(index+1, z)
    sum = sum + z

print(sum)