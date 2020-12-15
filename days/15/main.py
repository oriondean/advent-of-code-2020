from collections import defaultdict

if __name__ == '__main__':
    input = [9, 6, 0, 10, 18, 2, 1]
    seen = defaultdict(list)
    last_spoken = 0

    for i in range(0, 30000000):
        value = input[i % len(input)]

        last_spoken = value if i < len(input) else seen.get(last_spoken)[1] - seen.get(last_spoken)[0] if \
            seen.get(last_spoken)[1] >= len(input) else 0
        seen[last_spoken] = [seen[last_spoken][1], i] if seen[last_spoken] else [i, i]

        if i + 1 == 2020:
            print('Part one', last_spoken)

    print('Part two', last_spoken)
