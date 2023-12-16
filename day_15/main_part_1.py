filename = "day_15/input"

with open(filename) as file:
    lines = [line.rstrip() for line in file]

print(len(lines))
line = lines[0]
line_split = line.split(",")

sum = 0

for step in line_split:
    # print(step)

    current_value = 0

    for step_char in step:

        ascii_value = ord(step_char)
        current_value += ascii_value
        current_value *= 17
        current_value %= 256

    sum += current_value

print(sum)