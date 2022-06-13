

def pad(numeral:int):
    """A simple function to pad an integer with a leading zero if it is only 1 numeral long.

    Args:
        numeral (int): a single-digit integer that requires a leading 0 for padding.

    Returns:
        _str_: _a two-numeral-long string with a leading zero and the original argument as the right-most digit._
    """
    to_pad = str(numeral)           # convert the integer argument to a string so a leading "0" can be added
    if len(to_pad) == 1:            # check if padding is needed so the function can be used in a loop
        padded = "0" + to_pad       # create a new variable with the padded number
        return padded               # return the padded number.
    else:
        return to_pad               # return the unpadded double-digit string if it didn't require padding.

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
    
def axis_grid():
    x_axis = range(1,11)
    y_axis = range(1,11)
    
    top_axis = "____|"
    for x in x_axis:
        if x < 10:
            top_axis += f"__{x}_|"
        else:
            top_axis += f"_{x}_|"
    print(top_axis)
    
    grid_component = "    ."
    
    side_axis = ""
    for y in y_axis:
        if y < 10:
            side_axis += f"__{y}_|{grid_component*10}\n"
        else:
            side_axis += f"_{y}_|{grid_component*10}\n"
    print(side_axis)

axis_grid()