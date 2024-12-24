from collections import defaultdict

import numpy as np

with open("RaceCondition_Data.txt") as file:
    data = np.array([list(row.strip()) for row in file], dtype='<U5')

start_pos = np.where(data == 'S')
position = start_pos

counter = 0
max_i, max_j = data.shape


def is_in_maze(i, j):
    return 0 <= i < max_i and 0 <= j < max_j


def get_neighbours(i, j):
    neighbours = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    return [neighbour for neighbour in neighbours if is_in_maze(*neighbour)]


while True:
    data[*position] = counter

    for neighbour in get_neighbours(*position):
        val = data[*neighbour]
        if val == '.' or val == 'E':
            position = neighbour
            counter += 1
            break

    if data[*position] == 'E':
        data[*position] = counter
        break

data = np.where(data == '#', '-1', data).astype(int)
length0 = data.max()
count = 0
for i in range(length0+1):
    pos = np.where(data == i)
    for neighbour in get_neighbours(*pos):
        for next_neighbour in get_neighbours(*neighbour):
            val = int(data[*next_neighbour][0])
            if i + 100 < val:
                count += 1
print(count)



