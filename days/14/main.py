import re, math
from functools import reduce

regex_command_parse = re.compile('mem\[(\d+)\] = (\d+)')


def parse_command(raw_command):
    command = re.match(regex_command_parse, raw_command.strip())
    return int(command.group(1)), int(command.group(2))


def initialize_v1(lines):
    register = {}

    for line in lines:
        if line.startswith('mask'):
            mask = line.split(' = ')[1]
            mask_on = int('0b' + mask.replace('X', '0'), 2)
            mask_off = int('0b' + mask.replace('X', '1'), 2)
        else:
            [addr, value] = parse_command(line)
            register[addr] = (value | mask_on) & mask_off

    return register


def initialize_v2(lines):
    register = {}

    for line in lines:
        if line.startswith('mask'):
            mask = line.split(' = ')[1]
            mask_on = int('0b' + mask.replace('X', '0'), 2)
        else:
            [addr, value] = parse_command(line)
            addr_overwritten: str = bin((addr | mask_on))[2:].zfill(36)
            mask_floating = [i for i, c in list(enumerate(mask)) if c == 'X']

            overwrite_combinations = [
                [(math.floor(a / (2 ** (b - 1))) % 2) for b in range(len(mask_floating), 0, -1)]
                for a in range(0, 2 ** len(mask_floating))
            ]

            for combination in overwrite_combinations:
                r = list(addr_overwritten)
                for i in list(zip(mask_floating, combination)):
                    r[i[0]] = str(i[1])

                register[int('0b' + ''.join(r), 2)] = value

    return register


if __name__ == '__main__':
    register = {}

    with open('input.txt') as file:
        lines = [line.strip() for line in file]
    file.close()

    print('Part one', reduce(lambda memo, value: memo + value, initialize_v1(lines).values()))
    print('Part two', reduce(lambda memo, value: memo + value, initialize_v2(lines).values()))
