import re
from itertools import product
from math import prod

with open("RestroomRedoubt_Data.txt") as file:
    raw_data = file.readlines()
max_x, max_y = 101, 103
seconds = 100
data = [tuple(int(val) for val in re.match(r'p=([-\d]+),([-\d]+) v=([-\d]+),([-\d]+)', line).groups())
        for line in raw_data]
final_map = [[0 for _ in range(max_x)] for _ in range(max_y)]

for x0, y0, vx, vy in data:
    x = (x0 + vx * seconds) % max_x
    y = (y0 + vy * seconds) % max_y
    final_map[y][x] += 1

mid_col, mid_row = max_x // 2, max_y // 2

ranges = {
    "top-left": (range(0, mid_row), range(0, mid_col)),
    "top-right": (range(0, mid_row), range(mid_col + 1, max_x)),
    "bottom_left": (range(mid_row + 1, max_y), range(0, mid_col)),
    "bottom-right": (range(mid_row + 1, max_y), range(mid_col + 1, max_x))
}


def get_quadrant_sum(quadrant):
    return sum(final_map[y][x] for y, x in product(*ranges[quadrant]))


print(prod(get_quadrant_sum(quadrant) for quadrant in ranges))
