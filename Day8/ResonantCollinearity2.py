import itertools
from collections import defaultdict

import numpy as np

with open("ResonantCollinearity_Data.txt") as file:
    data = np.array([[val for val in line.strip()] for line in file.readlines()])

antenna_dict = defaultdict(list)
for i, line in enumerate(data):
    for j, value in enumerate(line):
        if value != '.':
            antenna_dict[value].append((i, j))

result_data = np.copy(data)
for key in antenna_dict:
    for permutation in itertools.permutations(antenna_dict[key], 2):
        (i_a, j_a), (i_b, j_b) = permutation
        coordinates = [(i_a + (i_a - i_b) * z, j_a + (j_a - j_b) * z) for z in range(-50, 50)]
        for i, j in coordinates:
            if 0 <= i < data.shape[0] and 0 <= j < data.shape[1]:
                result_data[i][j] = "#"
print(np.where(result_data == "#")[0].size)
