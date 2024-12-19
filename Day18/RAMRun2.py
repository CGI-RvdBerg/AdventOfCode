from operator import mul
import numpy as np

with open("RAMRun_Data.txt") as file:
    data = [[int(x) for x in line.strip().split(',')] for line in file.readlines()]

start = (0, 0)
stop = (70, 70)
size = (stop[0] + 1, stop[1] + 1)
time = 1024
max_steps = mul(*size)
check_val = max_steps * 2


def is_in_maze(x, y):
    return 0 <= x < size[0] and 0 <= y < size[1]


def get_neighbours(x, y):
    neighbours = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    return [neighbour for neighbour in neighbours if is_in_maze(*neighbour)]


def get_first_min_node(array):
    return np.unravel_index(array.argmin(), array.shape)


while True:
    maze = np.array([[max_steps for x in range(size[0])] for y in range(size[1])])
    for x, y in data[:time]:
        maze[x, y] = check_val
    maze[*start] = 0

    while True:
        current_node = get_first_min_node(maze)
        distance = maze[*current_node]
        for node in get_neighbours(*current_node):
            val = maze[*node]
            if val <= max_steps:
                maze[*node] = min(val, distance + 1)
        if current_node != stop and np.any(maze < max_steps):
            maze[*current_node] = check_val
        else:
            break

    if maze[*stop] == max_steps:
        print(time, data[time - 1])
        break
    else:
        time += 1
