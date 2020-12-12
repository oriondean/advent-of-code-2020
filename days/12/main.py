def execute_facing(instruction, position, facing):
    new_position = position.copy()
    [action, value] = instruction

    if action == 'F':
        action = 'N' if facing == 0 else 'E' if facing == 90 else 'S' if facing == 180 else 'W'

    if action in ['N', 'S']:
        new_position[1] += (value if action == 'N' else -value)
    elif action in ['E', 'W']:
        new_position[0] += (value if action == 'E' else -value)
    elif action in ['L', 'R']:
        facing += (value if action == 'R' else -value)
        facing %= 360

    return new_position, facing


def execute_waypoint(instruction, position_ship, position_waypoint):
    new_ship_position = position_ship.copy()
    new_waypoint_position = position_waypoint.copy()
    [action, value] = instruction

    if action in ['N', 'S']:
        new_waypoint_position[1] += (value if action == 'N' else -value)
    elif action in ['E', 'W']:
        new_waypoint_position[0] += (value if action == 'E' else -value)
    elif action in ['L', 'R']:
        while value > 0:
            new_waypoint_position = [
                new_waypoint_position[1] if action == 'R' else -new_waypoint_position[1],
                new_waypoint_position[0] if action == 'L' else -new_waypoint_position[0]
            ]
            value -= 90
    elif action == 'F':
        new_ship_position[0] += (new_waypoint_position[0] * value)
        new_ship_position[1] += (new_waypoint_position[1] * value)

    return new_ship_position, new_waypoint_position


if __name__ == '__main__':
    position = [0, 0]
    facing = 90

    position_ship = [0, 0]
    position_waypoint = [10, 1]

    with open('input.txt') as file:
        instructions = [(i[0], int(i[1:])) for i in [line.strip() for line in file]]
    file.close()

    for instruction in instructions:
        (position, facing) = execute_facing(instruction, position, facing)
        (position_ship, position_waypoint) = execute_waypoint(instruction, position_ship, position_waypoint)

    print('Part one', abs(position[0]) + abs(position[1]))
    print('Part two', abs(position_ship[0]) + abs(position_ship[1]))
