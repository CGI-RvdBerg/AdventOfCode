import itertools
from collections import defaultdict

import numpy


def do_part_1(raw_data):
    data = numpy.array([[letter for letter in line] for line in raw_data.split('\n')], dtype=str)

    # crop_data = {crop:numpy.array(numpy.where(data == crop),dtype=int) for crop in numpy.unique(data)}

    def find_contiguous_neighbours(coords, plot=None, crop0=None):
        if plot is None:
            plot = {"yx": set(), "perimeter":0}
        y0, x0 = coords
        if crop0 is None:
            crop0 = data[y0][x0]
        neighbour_coords = {
            'top': (y0 - 1, x0),
            'bottom': (y0 + 1, x0),
            'left': (y0, x0 + 1),
            'right': (y0, x0 - 1),
        }
        plot['yx'].add((y0, x0))
        fence = 4
        for y, x in list(neighbour_coords.values()):
            if 0 <= y < data.shape[0] and 0 <= x < data.shape[1]:
                if data[y][x] == crop0:
                    fence -= 1
                    if (y, x) not in plot['yx']:
                        plot['yx'].add((y, x))
                        for neighbour in find_contiguous_neighbours((y, x), plot, crop0)['yx']:
                            plot['yx'].add(neighbour)
        plot['perimeter'] += fence
        return plot

    checked_coords = set()
    count = 0
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if (i, j) not in checked_coords:
                plot = find_contiguous_neighbours((i, j))
                count += plot['perimeter']*len(plot['yx'])
                for coord in plot['yx']:
                    checked_coords.add(coord)
    return count



if __name__ == '__main__':
    with open("GardenGroups_Data.txt") as file:
        raw_data = file.read()
    print(do_part_1(raw_data))
