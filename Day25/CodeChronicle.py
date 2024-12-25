import itertools


def get_heights(lock_key):
    heights = [-1 for _ in range(len(lock_key[0]))]
    for row in lock_key:
        for i, val in enumerate(row):
            if val == '#':
                heights[i] += 1
    return tuple(heights)


with open("CodeChronicle_Data.txt") as file:
    data = [[row for row in lock_key.split("\n")] for lock_key in file.read().split("\n\n")]


locks, keys = set(), set()
for lock_key in data:
    if all(val == '.' for val in lock_key[0]):
        keys.add(get_heights(lock_key))
    else:
        locks.add(get_heights(lock_key))

count = 0
for lock, key in itertools.product(locks, keys):
    if not any(5<sum(cols) for cols in zip(lock, key)):
        count += 1
print(count)