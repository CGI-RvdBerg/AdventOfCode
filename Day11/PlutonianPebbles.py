def process_stone(stone):
    if int(stone) == 0:
        return "1"
    elif len(stone) % 2 == 0:
        i = len(stone) // 2
        return str(int(stone[:i])), str(int(stone[i:]))
    else:
        return str(int(stone) * 2024)


def unpack_stones(processed_stones):
    unpacked_stones = []
    for stone_pack in processed_stones:
        if type(stone_pack) is str:
            unpacked_stones.append(stone_pack)
        else:
            for stone in stone_pack:
                unpacked_stones.append(stone)
    return unpacked_stones


with open("PlutonianPebbles_Data.txt") as file:
    stones = file.readline().split(" ")

for _ in range(25):
    stones = unpack_stones(process_stone(stone) for stone in stones)
print(len(stones))
