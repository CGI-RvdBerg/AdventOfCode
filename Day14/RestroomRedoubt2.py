import re
from itertools import product
from math import prod
from numpy import array, uint8
from PIL import Image

with open("RestroomRedoubt_Data.txt") as file:
    raw_data = file.readlines()
max_x, max_y = 101, 103
max_seconds = max_x * max_y
data = [tuple(int(val) for val in re.match(r'p=([-\d]+),([-\d]+) v=([-\d]+),([-\d]+)', line).groups())
        for line in raw_data]

for ranger in (range(89, max_seconds, max_x), range(30, max_seconds, max_y)):
    for seconds in ranger:
        final_map = [[0 for _ in range(max_x)] for _ in range(max_y)]
        for x0, y0, vx, vy in data:
            x = (x0 + vx * seconds) % max_x
            y = (y0 + vy * seconds) % max_y
            final_map[y][x] += 1
        image_map = [[255 if value < 1 else 0 for value in row] for row in final_map]
        Image.fromarray(array(image_map, dtype=uint8), mode="L").save(f'{seconds}.png')
