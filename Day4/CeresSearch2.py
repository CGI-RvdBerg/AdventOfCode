import numpy as np


def is_mas(line):
    searchline = "".join(line)
    return searchline == "MAS" or searchline[::-1] == "MAS"


def is_x_mas(square):
    diagonal = np.diag(square)
    antidiagonal = np.diag(np.rot90(square))
    return is_mas(diagonal) and is_mas(antidiagonal)


with open("CeresSearch_Data.txt") as f:
    data = [[letter for letter in line.strip()] for line in f.readlines()]
    count = 0
    size = len(data[0])
    for i in range(size-2):
        lines = data[i:i+3]
        for j in range(size-2):
            square = np.array([line[j:j+3] for line in lines])
            if is_x_mas(square):
                count += 1
    print(count)



