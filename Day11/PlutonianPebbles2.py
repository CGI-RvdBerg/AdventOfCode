from collections import defaultdict


def process_stone(stone):
    if int(stone) == 0:
        return "1", None
    elif len(stone) % 2 == 0:
        i = len(stone) // 2
        return str(int(stone[:i])), str(int(stone[i:]))
    else:
        return str(int(stone) * 2024), None


with open("PlutonianPebbles_Data.txt") as file:
    stones = file.readline().split(" ")

stones_dict = defaultdict(lambda: 0)

for start_stone in stones:
    stones_dict[start_stone] += 1

for _ in range(75):
    old_stones_dict = stones_dict.copy()
    for old_stone in old_stones_dict:
        stones_dict[old_stone] -= old_stones_dict[old_stone]
        for new_stone in process_stone(old_stone):
            if new_stone is not None:
                stones_dict[new_stone] += old_stones_dict[old_stone]
print(sum(stones_dict.values()))
