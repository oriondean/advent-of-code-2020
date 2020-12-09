from functools import reduce


def has_sum_within(to_sum: list[int], value: int) -> bool:
    for i, x in enumerate(to_sum):
        for j, y in enumerate(to_sum):
            if i == j:
                continue

            if x + y == value:
                return True
    return False


def find_sum_range(to_sum: list[int], value: int) -> list[int]:
    start, end = 0, 1
    sum_of_range = to_sum[start] + to_sum[end]

    while sum_of_range != value:
        end += 1

        if end == len(to_sum) or sum_of_range > value:
            start += 1
            end = start + 1

        sum_of_range = reduce(lambda x, y: x + y, to_sum[start:end])

    return to_sum[start:end]


if __name__ == '__main__':
    with open('input.txt') as file:
        values: list[int] = [int(line) for line in file.read().split('\n')]
    file.close()

    preamble: int = 25
    non_sums: list[int] = [n for i, n in enumerate(values[preamble:]) if not has_sum_within(values[i:i+preamble], n)]
    sum_range: list[int] = find_sum_range(values, non_sums[0])

    print('Part one', non_sums[0])
    print('Part two', min(sum_range) + max(sum_range))
