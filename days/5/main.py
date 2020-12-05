import math
from itertools import chain

if __name__ == '__main__':
    highest_seat_id: int = 0
    seat_map = [[i for i in range(8)] for j in range(128)]

    with open('input.txt') as file:
        for line in file:
            row_range: [int, int] = [0, 127]
            column_range: [int, int] = [0, 7]
            for char in line:
                if char == 'F' or 'B':
                    delta = math.ceil((row_range[1] - row_range[0]) / 2) * (-1 if char == 'F' else 1)
                    row_range[1 if char == 'F' else 0] += delta
                if char == 'L' or 'R':
                    delta = math.ceil((column_range[1] - column_range[0]) / 2) * (-1 if char == 'L' else 1)
                    column_range[1 if char == 'L' else 0] += delta

            seat_id = row_range[0] * 8 + column_range[0]
            seat_map[row_range[0]][column_range[0]] = seat_id

            if seat_id > highest_seat_id:
                highest_seat_id = seat_id

    file.close()

    seat_list = list(chain.from_iterable(seat_map))[50:-50]  # chop off potentially non-existing seats
    index = 0
    while seat_list[index] == (seat_list[index + 1] - 1):
        index += 1

    print('Part one', highest_seat_id)
    print('Part two', seat_list[index + 1])
