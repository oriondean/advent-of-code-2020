import functools
from itertools import chain


def read_groups():
    groups: list[list[str]] = []
    with open('input.txt') as file:
        group: list[str] = []
        for rawLine in file:
            if rawLine.strip() == '':
                groups.append(group)
                group = []
            else:
                group.append(rawLine.strip())
        groups.append(group)
    file.close()
    return groups


if __name__ == '__main__':
    groups: list[list[str]] = read_groups()

    result_one = 0
    result_two = 0

    for group in groups:
        result_one += len(set(chain.from_iterable(group)))
        result_two += len(functools.reduce(lambda memo, value: [c for c in memo if c in value], group, group[0]))

    print('Part one', result_one)
    print('Part two', result_two)
