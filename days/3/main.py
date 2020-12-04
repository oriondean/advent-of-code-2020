import functools


def populate_map():
    slope_map: list[list[str]] = []
    with open('input.txt') as file:
        for line in file:
            slope_map.append(list(line)[0:-1])
        file.close()
    return slope_map


def traverse_map(traversal: [int, int]) -> int:
    position: [int, int] = [0, 0]  # [x, y]
    trees_encountered: int = 0

    while position[1] < len(slopeMap):
        if slopeMap[position[1]][position[0]] == '#':
            trees_encountered += 1
        position = [(position[0] + traversal[0]) % len(slopeMap[0]), position[1] + traversal[1]]

    return trees_encountered


if __name__ == '__main__':
    slopeMap: list[list[str]] = populate_map()
    mapDimensions: [int, int] = [len(slopeMap[0]), len(slopeMap)]  # [width, height]
    traversals: list[[int, int]] = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]  # [x, y]

    print('Part one', traverse_map(traversals[1]))
    print('Part two', functools.reduce(lambda a, b: a*b, map(traverse_map, traversals)))