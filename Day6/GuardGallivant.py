import numpy as np

with open("GuardGallivant_Data.txt") as file:
    data = np.array([[char for char in line.strip()] for line in file])
    y, x = np.where(data == "^")
    i = 0
    while 0 <= x < data.shape[1] and 0 <= y < data.shape[0]:
        def get_new_coord():
            match i:
                case 0:  # Up
                    return x, y - 1
                case 1:  # Right
                    return x + 1, y
                case 2:  # Down
                    return x, y + 1
                case 3:  # Left
                    return x - 1, y


        new_x, new_y = get_new_coord()
        try:
            next_step = data[new_y, new_x]
        except IndexError:
            pass

        if next_step == "#":
            i = (i + 1) % 4
        else:
            print(x, y)
            data[y, x] = 'X'
            x, y = get_new_coord()
    print(np.where(data == "X")[0].size)
