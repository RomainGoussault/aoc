import sys


def get_next_node(current_node, graph, instruction):

    destinations = graph[current_node]

    if instruction == "L":
        next_node = destinations[0]
    elif instruction == "R":
        next_node = destinations[1]
    else:
        raise Exception("Instruction not recognized")

    return next_node


filename = "day_8/input.csv"

with open(filename) as file:
    lines = [line.rstrip() for line in file]

instructions = lines[0]
# print(instructions)

graph_lines = lines[2:]
# print(graph_lines)

graph = {}
for graph_line in graph_lines:
    start_node_str, destinations_str = graph_line.replace(" ", "").split("=")
    destinations_str = destinations_str.replace("(", "").replace(")", "")
    graph[start_node_str] = destinations_str.split(",")


steps = 0
current_node = graph_lines[0][0:3]

while True:

    for instruction in instructions:
        # print(instruction)
        current_node = get_next_node(current_node, graph, instruction)
        steps += 1
        # print(current_node)

        if current_node == "ZZZ":
            print("steps", steps)
            sys.exit()


