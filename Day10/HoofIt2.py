import numpy as np


def get_data_bounded(data, i, j):
    if 0 <= i < data.shape[0] and 0 <= j < data.shape[1]:
        return data[i, j]
    else:
        return np.nan


with open("HoofIt_Data.txt") as file:
    data = np.array([[int(height) for height in line.strip()] for line in file])
    count = 0

    trailhead_locs = np.where(data == 0)
    for i, j in zip(*trailhead_locs):
        peaks = []


        def take_next_step_from(i, j, current_height):
            neighbour_locations = {
                "up": (i - 1, j),
                "down": (i + 1, j),
                "left": (i, j - 1),
                "right": (i, j + 1)
            }
            for new_i, new_j in neighbour_locations.values():
                new_height = get_data_bounded(data, new_i, new_j)
                if current_height == 8 and new_height == 9:
                    peaks.append((new_i, new_j))
                elif new_height == current_height + 1:
                    take_next_step_from(new_i, new_j, new_height)


        take_next_step_from(i, j, 0)
        count += len(peaks)
print(count)