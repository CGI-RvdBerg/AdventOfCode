import re

with open("MullItOver_Data.txt") as file:
    score = 0
    for line in file:
        muls = re.findall(r'mul\((\d+),(\d+)\)', line)
        for x, y in muls:
            score += int(x) * int(y)
    print(score)
