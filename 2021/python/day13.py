import time

with open("../input/day13_sample.txt", "r") as fp:
    file_data = [line.rstrip() for line in fp.readlines()]


def with_perf_timing(fn, args=None):
    start_time = time.perf_counter()
    if args:
        fn(args)
    else:
        fn()
    end_time = time.perf_counter()
    print(f'Execution time: {end_time - start_time:0.6f}')


def to_fold_instruction(line):
    fold_along_direction, distance = line.split('=')
    direction = fold_along_direction[-1]
    distance = int(distance)
    return direction, distance


def lines_to_instructions(lines):
    draw_instructions = []
    fold_instructions = []
    for line in lines:
        if line.startswith("fold"):
            fold_instructions.append(to_fold_instruction(line))
        else:
            if len(line) > 0:
                x, y = [int(i) for i in line.split(',')]
                draw_instructions.append([x, y])

    return draw_instructions, fold_instructions


def fold(draw_instructions, fold_instruction):
    direction, distance = fold_instruction
    fold_position = 0 if direction == 'x' else 1

    for draw_instruction in [i for i in draw_instructions if i[fold_position] > distance]:
        draw_instruction[fold_position] = 2 * distance - draw_instruction[fold_position]
    return


def draw(instructions):
    for instruction in instructions:
        print(instruction)

    print(f'drawn from {len(instructions)} instructions')
    return


def part1():
    draw_instructions, fold_instructions = lines_to_instructions(file_data)

    fold(draw_instructions, fold_instructions[0])

    applicable_instructions = []
    for i in draw_instructions:
        if i not in applicable_instructions and i[0] >= 0 and i[1] >= 0:
            applicable_instructions.append(i)

    applicable_instructions.sort()
    draw(applicable_instructions)

    return


if __name__ == "__main__":
    with_perf_timing(part1)
    # 790
