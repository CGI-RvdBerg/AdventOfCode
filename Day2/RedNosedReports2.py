from itertools import pairwise

safe_reports = 0
with open("RedNosedReports_Data.txt") as file:
    for line in file:
        levels = [int(level) for level in line.split(" ")]
        if levels == sorted or levels[::-1] == sorted:
            is_safe = True
            for current_val, next_val in pairwise(levels):
                if not 4 > abs(current_val - next_val) > 0:
                    is_safe = False
                    break
            safe_reports += 1 if is_safe else 0
print(safe_reports)