from itertools import pairwise


def check_safe(levels):
    return all(
        4 > (x - x_next) > 0 for x, x_next in pairwise(levels)
    ) or all(
        0 > (x - i_next) > -4 for x, x_next in pairwise(levels)
    )


with open("RedNosedReports_Data.txt") as file:
    data = [[int(level) for level in line.split(" ")] for line in file]
    print(sum(check_safe(levels) for levels in data))
