def mineLocation(field):
    '''
    This function accepts a 'field' tuple, consisting of coords like:
    [
      [1, 0, 0],
      [0, 0, 0],
      [0, 0, 0]
    ]
    The mine is represented by a 1, and the location is given as [x, y].
    The example above's location would be returned by this function as:
    [0, 0]
    :param field:
    :return:
    '''

    # Increment the x, y coords when the row doesn't find it's match
    coord = [3, -1]
    i = 0
    grid_width = len(field[0])
    while i < grid_width:
        for j in field[i]:
            coord[1] += 1  # Increment each time the column is empty
            if j == 1:
                coord[0] = i
                coord[1] = coord[1] % grid_width
                return coord
        i += 1

mine = [[1, 0, 0],[0, 0, 0],[0, 0, 0]]
print mineLocation(mine)
