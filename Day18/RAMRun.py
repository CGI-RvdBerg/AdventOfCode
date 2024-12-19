from operator import mul
import numpy as np

start = (0, 0)
stop = (6, 6)
size = (stop[0] + 1, stop[1] + 1)
time = 12
max_steps = mul(*size)
check_val = max_steps*2


def is_in_maze(x, y):
    return 0 <= x < size[0] and 0 <= y < size[1]


def get_neighbours(x, y):
    neighbours = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    return [neighbour for neighbour in neighbours if is_in_maze(*neighbour)]


def get_first_min_node(array):
    return np.unravel_index(array.argmin(), array.shape)


with open("RAMRun_Data.txt") as file:
    data = [[int(x) for x in line.strip().split(',')] for line in file.readlines()]

maze = np.array([[max_steps for x in range(size[0])] for y in range(size[1])])
for x, y in data[:time]:
    maze[x, y] = check_val

maze[*start] = 0
current_node = start
while current_node != stop:
    current_node = get_first_min_node(maze)
    distance = maze[*current_node]
    for node in get_neighbours(*current_node):
        val = maze[*node]
        if val <= max_steps:
            maze[*node] = min(val, distance + 1)
    maze[*current_node] = check_val
print(distance)