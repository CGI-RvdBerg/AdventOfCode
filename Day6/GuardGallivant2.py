import itertools

import numpy as np

with open("GuardGallivant_Data.txt") as file:
    original_data = np.array([[char for char in line.strip()] for line in file])

y0, x0 = np.where(original_data == "^")
shape = original_data.shape
count = 209
for a, b in itertools.product(range(17, shape[0]), range(shape[1])):
    data = original_data.copy()
    data[a, b] = "#"
    steps = []
    x, y = x0, y0
    i = 0
    while 0 <= x < shape[1] and 0 <= y < shape[0]:
        def get_new_coord():
            match i:
                case 0:  # Up
                    return x, y - 1
                case 1:  # Right
                    return x + 1, y
                case 2:  # Down
                    return x, y + 1
                case 3:  # Left
                    return x - 1, y


        new_x, new_y = get_new_coord()
        try:
            next_step = data[new_y, new_x]
        except IndexError:
            pass

        if next_step == "#":
            step = (x, y, i)
            if step in steps:
                count += 1
                print((a, b), count)
                break
            else:
                steps.append((x, y, i))
                i = (i + 1) % 4
        else:
            x, y = get_new_coord()
