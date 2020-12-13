from math import ceil


if __name__ == '__main__':
    with open('input.txt') as file:
        earliest_departure = int(file.readline().strip())
        timetable = ['x' if i == 'x' else int(i) for i in file.readline().strip().split(',')]

    file.close()

    closest_times = sorted(
        [(ceil(earliest_departure / time) * time, time) for time in filter(lambda value: value != 'x', timetable)])
    print('Part one', (closest_times[0][0] - earliest_departure) * closest_times[0][1])

    timetable = list(filter(lambda value: value[1] != 'x', enumerate(timetable)))
    full_sequence_found = False
    time = 0

    increment = timetable[0][1]
    highest_seen_passed = (0, 0, False)  # (passed count, time, seen before)

    while not full_sequence_found:
        time += increment

        sequence_count = len("".join(['F' if (time + i) % n else 'T' for i, n in timetable[1:]]).split('F')[0])
        if sequence_count > highest_seen_passed[0]:
            highest_seen_passed = (sequence_count, time, True)
        elif sequence_count == highest_seen_passed[0] and highest_seen_passed[2]:
            increment = (time - highest_seen_passed[1])
            highest_seen_passed = (sequence_count, time, False)

        full_sequence_found = (sequence_count == len(timetable[1:]))

    print('Part two', time)
