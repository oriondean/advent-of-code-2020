def parse(raw_instruction):
    parsed = raw_instruction.split(' ')
    return {
        'operation': parsed[0],
        'value': int(parsed[1][1:]) if parsed[1].startswith('+') else int(parsed[1]),
        'executedCount': 0
    }


def run(instructions):
    for instruction in instructions:
        instruction['executedCount'] = 0

    accumulator = 0
    cursor = 0
    instruction_previously_seen = False
    while not instruction_previously_seen and cursor < len(instructions):
        instruction = instructions[cursor]

        if instruction['executedCount'] == 1:
            instruction_previously_seen = True
            break

        if instruction['operation'] == 'acc':
            accumulator += instruction['value']
        if instruction['operation'] == 'jmp':
            cursor += instruction['value'] - 1

        cursor += 1
        instruction['executedCount'] += 1

    return instruction_previously_seen, accumulator


if __name__ == '__main__':
    with open('input.txt') as file:
        instructions = [parse(i) for i in file.read().split('\n')]
        file.close()

    print('Part one', run(instructions)[1])

    has_flipped_operation = False
    cursor = 0

    while run(instructions)[0]:
        if has_flipped_operation:
            instructions[cursor]['operation'] = 'nop' if instructions[cursor]['operation'] == 'jmp' else 'jmp'
            cursor += 1
            has_flipped_operation = False

        if instructions[cursor]['operation'] in ['nop', 'jmp']:
            instructions[cursor]['operation'] = 'nop' if instructions[cursor]['operation'] == 'jmp' else 'jmp'
            has_flipped_operation = True
        else:
            cursor += 1  # iterate through instructions until a nop/jmp encountered

    print('Part two', run(instructions)[1])
