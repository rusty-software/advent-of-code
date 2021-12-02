with open("../input/day02.txt", "r") as fp:
    instructions = [line.rstrip() for line in fp.readlines()]


def part1():
    position = [0, 0]
    for instruction in instructions:
        direction, quantity = instruction.split(' ')
        if direction == 'forward':
            position[0] += int(quantity)
        elif direction == 'down':
            position[1] += int(quantity)
        else:
            position[1] -= int(quantity)

    print(f'Position[horizontal, depth]: {position}; product: {position[0] * position[1]}')
    return


if __name__ == "__main__":
    part1()
    # 1752
    # part2()
    # 1781
