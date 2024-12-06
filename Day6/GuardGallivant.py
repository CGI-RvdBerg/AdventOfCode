import numpy as np

with open("GuardGallivant_Data.txt") as file:
    data = np.array([[char for char in line.strip()] for line in file])
    x, y = np.where(data == "^")
    i = 0
    while x < data.shape[0] and y < data.shape[1]:
        def get_new_coord():
            match i:
                case 0:
                    return x, y-1
                case 1:
                    return x-1, y
                case 2:
                    return x, y+1
                case 3:
                    return x+1, y
        new_x, new_y = get_new_coord()
        try:
            next_step = data[new_x, new_y]
        except IndexError:
            print('Index out of range')

        if next_step == "#":
            i = (i+1) % 4
        else:
            data[x,y] = 'X'
            x, y = get_new_coord()
    print(np.where(data == "X"))


