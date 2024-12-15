import itertools
from collections import defaultdict

import numpy as np
with open("ResonantCollinearity_Data.txt") as file:
    data = np.array([[val for val in line.strip()] for line in file.readlines()])
    result_data = np.copy(data)

    antenna_dict = defaultdict(list)
    for i, line in enumerate(data):
        for j, value in enumerate(line):
            if value != '.':
                antenna_dict[value].append((i, j))

    for key in antenna_dict:
        for permutation in itertools.permutations(antenna_dict[key],2):
            (i_a, j_a), (i_b, j_b) = permutation
            i1, j1 = 2*i_a - i_b, 2*j_a - j_b
            i2, j2 = 2*i_b - i_a, 2*j_b - j_a
            for i, j in [(i1, j1), (i2, j2)]:
                if 0 <= i < data.shape[0] and 0 <= j < data.shape[1]:
                    result_data[i][j] = "#"
    print(np.where(result_data == "#")[0].size)