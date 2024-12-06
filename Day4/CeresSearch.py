import numpy as np


def countXMAS(line):
    searchline = "".join(line)
    return searchline.count("XMAS") + searchline[::-1].count("XMAS")


with open("CeresSearch_Data.txt") as f:
    data = np.array([[letter for letter in line.strip()] for line in f.readlines()])
    count = 0
    size = data.shape[0]
    for search_data in [data, np.rot90(data)]:
        for i in range(-size + 1, size):
            count += countXMAS(np.diag(search_data, i))
        for line in search_data:
            count += countXMAS(line)

    print(count)

