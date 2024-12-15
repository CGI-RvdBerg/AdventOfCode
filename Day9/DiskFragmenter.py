from itertools import zip_longest

with open("DiskFragmenter_Data.txt") as file:
    disk_map = [int(val) for val in file.readline().strip()]

files = disk_map[0::2]
free_spaces = disk_map[1::2]
file_ids = []
for i, (a, b) in enumerate(zip_longest(files, free_spaces, fillvalue=0)):
    for _ in range(a):
        file_ids.append(i)
    for _ in range(b):
        file_ids.append(None)

count = 0
i, j = 1, len(file_ids)-1
while i <= j:
    id = file_ids[i]
    if id is not None:
        count += i*id
    else:
        while file_ids[j] is None:
            j -= 1
        count += i*file_ids[j]
        j -= 1
    i += 1
print(count)