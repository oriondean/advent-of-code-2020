from collections import defaultdict


def get_neighbours(coord, is_4d):
    neighbours = []

    for x in range(coord[0] - 1, coord[0] + 2):
        for y in range(coord[1] - 1, coord[1] + 2):
            for z in range(coord[2] - 1, coord[2] + 2):
                if is_4d:
                    for q in range(coord[3] - 1, coord[3] + 2):
                        neighbours.append((x, y, z, q))
                else:
                    neighbours.append((x, y, z))

    return [c for c in neighbours if str(c) != str(coord)]


def expand_dimension(dimension, is_4d):
    new_dimension = dimension.copy()

    for coord in dimension:
        for coord2 in get_neighbours(coord, is_4d):
            new_dimension[coord2] = '.'

    return new_dimension


def iterate_dimension(dimension, is_4d):
    new_dimension = expand_dimension(dimension, is_4d)

    for coord in new_dimension:
        active_neighbours_count = len([c for c in get_neighbours(coord, is_4d) if dimension[c] == '#'])

        if dimension[coord] == '#':
            new_dimension[coord] = '#' if active_neighbours_count in [2, 3] else '.'
        else:
            new_dimension[coord] = '#' if active_neighbours_count == 3 else '.'

    return new_dimension


if __name__ == '__main__':
    dimension_3d = defaultdict(str)
    dimension_4d = defaultdict(str)

    with open('input.txt') as file:
        y = 0
        for line in file:
            for x, c in enumerate(line.strip()):
                dimension_3d[(x, y, 0)] = c
                dimension_4d[(x, y, 0, 0)] = c
            y += 1

    file.close()

    for i in range(0, 6):
        dimension_3d = iterate_dimension(dimension_3d, False)
        dimension_4d = iterate_dimension(dimension_4d, True)

    print('Part one', len([c for c in dimension_3d if dimension_3d[c] == '#']))
    print('Part two', len([c for c in dimension_4d if dimension_4d[c] == '#']))
