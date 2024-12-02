from itertools import pairwise
from RedNosedReports import check_safe

with open("RedNosedReports_Data.txt") as file:
    count = 0
    for line in file:
        levels = [int(level) for level in line.split(" ")]
        if check_safe(levels):
            count += 1
        else:
            for i in range(len(levels)):
                new_levels = levels[:i] + levels[i+1:]
                if check_safe(new_levels):
                    count += 1
                    break
    print(count)
