from collections import defaultdict

if __name__ == '__main__':
    with open('input.txt') as file:
        adaptors: list[int] = sorted([int(line) for line in file.read().split('\n')])
        adaptors.insert(0, 0)
        adaptors.append(max(adaptors) + 3)
    file.close()

    differences = defaultdict(int)
    for index, adaptor in enumerate(adaptors[:-1]):
        differences[adaptors[index + 1] - adaptors[index]] += 1
    print('Part one', differences[3] * differences[1])

    paths = defaultdict(int, {0: 1})
    for adaptor in adaptors[1:]:
        # sum up the numbers of distinct paths that can lead to connectable adaptors preceding current adaptor
        paths[adaptor] = paths[adaptor - 1] + paths[adaptor - 2] + paths[adaptor - 3]
    print('Part two', paths[max(paths.keys())])
