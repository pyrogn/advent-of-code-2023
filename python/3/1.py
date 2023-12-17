def neighbor_idx(data, r, c):
    coords = []
    for rc in (r - 1, r, r + 1):
        for cc in (c - 1, c, c + 1):
            if not (rc < 0 or cc < 0):
                coords.append((rc, cc))
    for coord in coords:
        try:
            data[coord[0]][coord[1]]
        except IndexError:
            coords.remove(coord)
    return coords


data = [i.strip() for i in open("3/input.txt")]
print(data)
