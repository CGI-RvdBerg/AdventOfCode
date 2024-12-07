import itertools

with open("PrintQueue_Data.txt") as file:
    count = 0
    lines = [line.strip() for line in file.readlines()]
    rules = [line.split("|") for line in lines if "|" in line]
    rules_set = {rule[0] for rule in rules}
    rules_dict = {rule: [] for rule in rules_set}
    for key, value in rules:
        rules_dict[key].append(value)

    updates = [line.split(",") for line in lines if "," in line]
    for line in updates:
        in_right_order = True
        for a, b in itertools.pairwise(line):
            try:
                if a in rules_dict[b]:
                    in_right_order = False
                    break
            except KeyError:
                pass
        if in_right_order:
            count += int(line[len(line) // 2])
print(count)