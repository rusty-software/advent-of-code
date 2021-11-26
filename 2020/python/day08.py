import copy

with open("../input/day08.txt", "r") as fp:
    lines = fp.readlines()
    lines = [line.rstrip() for line in lines]


def lines_to_instructions():
    instructions = []
    for line in lines:
        operation, rest = line.split(' ')
        direction = rest[0]
        amount = rest[1:]
        instructions.append({'operation': operation, 'direction': direction, 'amount': amount})

    return instructions


def more_valid_instructions(instructions, next_instruction_idx, executed_instruction_idxs):
    if next_instruction_idx >= len(instructions):
        # print(f'next_instruction_idx {next_instruction_idx} is out of bounds')
        return 'finished'

    if next_instruction_idx in executed_instruction_idxs:
        # print(f'next_instruction_idx {next_instruction_idx} already executed: {executed_instruction_idxs}')
        return 'infinite loop'

    return 'more instructions'


def try_instructions(instructions):
    executed_instruction_idxs = []
    next_instruction_idx = 0
    accumulated = 0
    instruction_result = 'more instructions'
    while instruction_result == 'more instructions':
        executed_instruction_idxs.append(next_instruction_idx)
        current_instruction = instructions[next_instruction_idx]

        operation = current_instruction.get('operation')
        if operation == 'nop':
            next_instruction_idx += 1
            continue

        direction = current_instruction.get('direction')
        amount = int(current_instruction.get('amount'))
        if operation == 'acc':
            if direction == '+':
                accumulated += amount
            else:
                accumulated -= amount
            next_instruction_idx += 1
        else:
            if direction == '+':
                next_instruction_idx += amount
            else:
                next_instruction_idx -= amount
        instruction_result = more_valid_instructions(instructions, next_instruction_idx, executed_instruction_idxs)

    return instruction_result, accumulated


def part1():
    instructions = lines_to_instructions()
    instruction_result, accumulated = try_instructions(instructions)

    print(f'Instructions result: {instruction_result}, accumulated: {accumulated}')
    return


def switch_operation(instructions, op_idx):
    instruction = instructions[op_idx]
    operation = instruction.get('operation')
    if operation == 'nop':
        instruction.update({'operation': 'jmp'})
    elif operation == 'jmp':
        instruction.update({'operation': 'nop'})

    instructions[op_idx] = instruction

    return


def part2():
    instructions = lines_to_instructions()
    nop_jmp_idxs = []
    for i, instruction in enumerate(instructions):
        operation = instruction.get('operation')
        if operation != 'acc':
            nop_jmp_idxs.append(i)

    print(f'nop_jmp_idxs_count: {len(nop_jmp_idxs)}')
    for op_idx in nop_jmp_idxs:
        new_instructions = copy.deepcopy(instructions)
        switch_operation(new_instructions, op_idx)
        instruction_result, accumulated = try_instructions(new_instructions)
        if instruction_result == 'finished':
            print(f'Finished successfully! Accumulated: {accumulated}')
            break

    print('Never managed to finish...')
    return


if __name__ == "__main__":
    # part1()
    # 1200
    part2()
    # 1023
