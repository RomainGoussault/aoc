filename = "day_15/input_test"

with open(filename) as file:
    lines = [line.rstrip() for line in file]

print(len(lines))
line = lines[0]
line_split = line.split(",")

sum = 0


class Lens:

    # Constructor method (initializer)
    def __init__(self, label, focal_length):
        # Instance attributes
        self.label = label
        self.focal_length = focal_length

    def __str__(self):
        return f"[{self.label} {self.focal_length}]"

    def __repr__(self):
        return f"[{self.label} {self.focal_length}]"


class Box:

    # Constructor method (initializer)
    def __init__(self, id, lens_list=[]):
        # Instance attributes
        self.id = id
        self.lens_list = lens_list

    def __str__(self):
        return f"[Box {self.id}] {self.lens_list}"

    def __repr__(self):
        return f"[Box {self.id}] {self.lens_list}"

    def is_empty(self):
        return len(self.lens_list) == 0

    def get_idx_of_lens(self, label):
 
        idx = None
        for i in range(0, len(self.lens_list)):
            if self.lens_list[i].label == label:
                idx = i
                break

        return idx

    def add_lens(self, lens):

        lens_found = False
        for lens in self.lens_list:
            if lens.label == label:
                lens.focal_length = focal_length
                lens_found = True
                break

        if not lens_found:
            self.lens_list.append(lens)

    def remove_lens(self, lens):

        idx = self.get_idx_of_lens(lens.label)
        if idx is not None:
            self.lens_list.pop(idx)


def print_box_list(box_list):
    for box in box_list:
        if not box.is_empty():
            print(box)


def HASH(label):

    result = 0

    for step_char in label:
        ascii_value = ord(step_char)
        result += ascii_value
        result *= 17
        result %= 256

    return result


box_list = []
for i in range(0, 256):
    box_list.append(Box(i))

box_list[1].add_lens(Lens("cm", 2))

for step in line_split:
    print_box_list(box_list)
    print(step)
    current_value = HASH(step)

    if "=" in step:

        label = step.split("=")[0]
        focal_length = step.split("=")[1]
        lens = Lens(label, focal_length)

        box_id = HASH(label)
        box = box_list[box_id]
        box.add_lens(lens)
    
    elif "-" in step:

        label = step.split("-")[0]
        focal_length = step.split("-")[1]
        lens = Lens(label, focal_length)

        box_id = HASH(label)
        box = box_list[box_id]
        box.remove_lens(lens)

    else:
        raise Exception("Invalid step")

