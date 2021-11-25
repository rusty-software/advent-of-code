with open("../input/day08.txt", "r") as fp:
    lines = fp.readlines()
    lines = [line.rstrip() for line in lines]


def more_valid_instructions(instructions, next_instruction_idx, executed_instruction_idxs):
    if next_instruction_idx < 0 or next_instruction_idx >= len(instructions):
        print(f'next_instruction_idx {next_instruction_idx} is out of bounds')
        return False

    if next_instruction_idx in executed_instruction_idxs:
        print(f'next_instruction_idx {next_instruction_idx} already executed: {executed_instruction_idxs}')
        return False

    return True


def part1():
    instructions = []
    for line in lines:
        operation, rest = line.split(' ')
        direction = rest[0]
        amount = rest[1:]
        instructions.append({'operation': operation, 'direction': direction, 'amount': amount})

    executed_instruction_idxs = []
    next_instruction_idx = 0
    accumulated = 0
    while more_valid_instructions(instructions, next_instruction_idx, executed_instruction_idxs):
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

    print(f'Accumulated: {accumulated}')
    return


if __name__ == "__main__":
    part1()
    # 1200
