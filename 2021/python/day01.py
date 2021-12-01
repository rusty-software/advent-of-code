with open("../input/day01.txt", "r") as fp:
    depths = [int(line.rstrip()) for line in fp.readlines()]


def part1():
    last_depth = depths[0]
    increases = 0
    for current_depth in depths:
        if current_depth > last_depth:
            increases += 1
        last_depth = current_depth
    print(f'Increases: {increases}')
    return


def part2():
    last_3_depth = sum(depths[:3])
    increases = 0
    for idx, current_depth in enumerate(depths):
        if idx > len(depths) - 3:
            break

        current_3_depth = sum(depths[idx:idx + 3])
        if current_3_depth > last_3_depth:
            increases += 1

        last_3_depth = current_3_depth

    print(f'Increases: {increases}')

    return


if __name__ == "__main__":
    # part1()
    # 1752
    part2()
    # 1781
