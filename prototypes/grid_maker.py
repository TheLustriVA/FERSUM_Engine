
from ast import Pass


def pad(numeral:int):
    to_pad = str(numeral)
    if len(to_pad) == 1:
        padded = "0" + to_pad
        return padded
    else:
        return to_pad

def simple_grid():
    x_coords = []
    y_coords = []

    for x_coord in range(1,11):
        x_coords.append(x_coord)
    for y_coord in range(1,11):
        y_coords.append(x_coords)
    for coord in y_coords: print(coord)

def coordinate_grid():
    grid = []
    grid_row = []
    for y_coord in range(1,11):
        for x_coord in range(1,11):
            print(type(x_coord))
            coords = [pad(y_coord), pad(x_coord)]
            grid_row.append(coords)
        grid.append(grid_row)
        grid_row = []
    for row in grid: print(row)

coordinate_grid()