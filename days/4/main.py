import functools
import re


def read_passports() -> list[dict]:
    with open('input.txt') as file:
        lines = file.read().split('\n\n')
    file.close()

    raw_passports = [re.split('\s', re.sub('\n', ' ', line.strip())) for line in lines]

    return list(map(
        lambda raw_passport: dict(functools.reduce(lambda memo, pair: memo + [pair.split(':')], raw_passport, [])),
        raw_passports))


def is_valid_simple(passport) -> bool:
    return len(passport) == 8 or (len(passport) == 7 and 'cid' not in passport)


def is_within_range(field: str, min: int, max: int) -> bool:
    return min <= int(field) <= max


def is_valid_height(height: str) -> bool:
    if re.fullmatch('\d{3}cm', height):
        result = 150 <= int(height[0:3]) <= 193
        return result

    if re.fullmatch('\d{2}in', height):
        result = 59 <= int(height[0:2]) <= 76
        return result

    return False


def is_valid_complex(passport) -> bool:
    return is_valid_simple(passport) and is_within_range(passport['byr'], 1920, 2002) and \
           is_within_range(passport['iyr'], 2010, 2020) and \
           is_within_range(passport['eyr'], 2020, 2030) and is_valid_height(passport['hgt']) and \
           re.fullmatch('#[0-9a-f]{6}', passport['hcl']) and \
           passport['ecl'] in str(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']) and \
           re.fullmatch('\d{9}', passport['pid'])


if __name__ == '__main__':
    passports = read_passports()

    print('Part one', len([p for p in passports[::-1] if is_valid_simple(p)]))
    print('Part two', len([p for p in passports[::-1] if is_valid_complex(p)]))
