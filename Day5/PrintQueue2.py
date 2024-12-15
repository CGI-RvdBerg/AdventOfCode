import itertools
from collections import defaultdict

with open("PrintQueue_Data.txt") as file:
    lines = [line.strip() for line in file.readlines()]

rules = [line.split("|") for line in lines if "|" in line]
rules_dict = defaultdict(list)
for key, value in rules:
    rules_dict[key].append(value)

count = 0
updates = [line.split(",") for line in lines if "," in line]
for line in updates:
    is_bad_line = False
    for a, b in itertools.pairwise(line):
        if a in rules_dict[b]:
            is_bad_line = True
            break
    if is_bad_line:
        for value in line:
            position = sum(1 for val in line if val in rules_dict[value])
            if position == len(line)//2:
                count += int(value)
print(count)