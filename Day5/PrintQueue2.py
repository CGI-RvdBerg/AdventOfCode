import itertools

with open("PrintQueue_Data1.txt") as file:
    count = 0
    lines = [line.strip() for line in file.readlines()]
    rules = [line.split("|") for line in lines if "|" in line]
    rules_set = {rule[0] for rule in rules}
    rules_dict = {rule: [] for rule in rules_set}
    for key, value in rules:
        rules_dict[key].append(value)

    updates = [line.split(",") for line in lines if "," in line]
    bad_lines = []
    for line in updates:
        for a, b in itertools.pairwise(line):
            try:
                if a in rules_dict[b]:
                    bad_lines.append(line)
                    break
            except KeyError:
                pass

    for line in bad_lines:
        pass
print(count)