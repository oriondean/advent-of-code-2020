from copy import deepcopy
from itertools import chain


def is_within_bounds(layout, row, col):
    return 0 <= row < len(layout) and 0 <= col < len(layout[0])


def count_adjacent_filled_seats(layout, row, col):
    seats = []

    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if is_within_bounds(layout, r, c):
                if (not r == row or not c == col) and layout[r][c] == '#':
                    seats.append(layout[r][c])

    return len(seats)


def count_visible_filled_seats(layout, row, col):
    seats = []

    for direction in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
        r = row + direction[0]
        c = col + direction[1]
        found_seat = False

        while is_within_bounds(layout, r, c) and not found_seat:
            if layout[r][c] != '.':
                found_seat = True
                seats.append(layout[r][c])

            r += direction[0]
            c += direction[1]

    return len([s for s in seats if s == '#'])


def update_layout(old_layout):
    size_row = len(old_layout)
    size_col = len(old_layout[0])
    seating_changes = 0
    new_layout = deepcopy(layout)

    for row in range(0, size_row):
        for col in range(0, size_col):
            if old_layout[row][col] == 'L':
                # switch around if statements for different parts
                # if count_adjacent_filled_seats(old_layout, row, col) == 0:
                if count_visible_filled_seats(layout, row, col) == 0:
                    seating_changes += 1
                    new_layout[row][col] = '#'
            if old_layout[row][col] == '#':
                # switch around if statements for different parts
                # if count_adjacent_filled_seats(old_layout, row, col) >= 4:
                if count_visible_filled_seats(layout, row, col) >= 5:
                    seating_changes += 1
                    new_layout[row][col] = 'L'

    return new_layout, seating_changes


if __name__ == '__main__':
    with open('input.txt') as file:
        layout = [list(line.strip()) for line in file]
    file.close()

    seating_changes = 1
    while seating_changes > 0:
        (layout, seating_changes) = update_layout(layout)

    print('occupied seats', len([seat for seat in list(chain.from_iterable(layout)) if seat == '#']))
