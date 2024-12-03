import re

with open("MullItOver_Data.txt") as file:
    score = 0
    enabled = True
    for line in file:
        matches = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", line)
        for x, y, do, dont in matches:
            if dont:
                enabled = False

            if do:
                enabled = True

            if enabled and not do:
                score += int(x) * int(y)

    print(score)
