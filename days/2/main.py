import re


def is_password_valid_frequency(password: str, letter: str, letter_frequency_range: [int, int]):
    return letter_frequency_range[0] <= password.count(letter) <= letter_frequency_range[1]


def is_password_valid_position(password: str, letter: str, position_policy: [int, int]):
    return int(is_character_at_index(password, letter, position_policy[0] - 1)) +\
           int(is_character_at_index(password, letter, position_policy[1] - 1)) == 1


def is_character_at_index(string: str, char: str, index: int):
    if 0 <= index < len(string):
        return string[index] == char
    return False


if __name__ == '__main__':
    lineRegex = re.compile('^(\d{1,2}-\d{1,2})\s(\w): (\w+)$')
    letterFrequencyRegex = re.compile('-')

    validFrequencyPasswords: int = 0
    validPositionPasswords: int = 0

    with open('input.txt') as file:
        for line in file:
            parsed = re.match(lineRegex, line)
            letterRange: [int, int] = list(map(int, re.split(letterFrequencyRegex, parsed.group(1))))

            if is_password_valid_frequency(parsed.group(3), parsed.group(2), letterRange):
                validFrequencyPasswords += 1

            if is_password_valid_position(parsed.group(3), parsed.group(2), letterRange):
                validPositionPasswords += 1

        file.close()

    print('Part one', validFrequencyPasswords)
    print('Part two', validPositionPasswords)
