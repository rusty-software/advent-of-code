file = open('../input/day03.txt', 'r')
lines = file.readlines()


def inc_x(x, step_x, line_len):
    next_x = x + step_x
    if next_x >= line_len:
        next_x -= line_len

    return next_x


def is_tree(x, line):
    return line[x] == '#'


def trees_hit(step_x, step_y):
    # always process the upper left coordinate
    x = 0
    y = 1
    next_y = 1
    hit_count = 0

    for line in lines:
        if y == next_y:
            line = line.replace('\n', '')
            hit_count += 1 if is_tree(x, line) else 0
            x = inc_x(x, step_x, len(line))
            next_y = y + step_y
        y += 1

    return hit_count


def part1():
    hit_count = trees_hit(3, 1)
    print('Trees hit: {:d}'.format(hit_count))


def part2():
    hits_1_1 = trees_hit(1, 1)
    print('Trees hit for right 1, down 1: {:d}'.format(hits_1_1))
    hits_3_1 = trees_hit(3, 1)
    print('Trees hit for right 3, down 1: {:d}'.format(hits_3_1))
    hits_5_1 = trees_hit(5, 1)
    print('Trees hit for right 5, down 1: {:d}'.format(hits_5_1))
    hits_7_1 = trees_hit(7, 1)
    print('Trees hit for right 7, down 1: {:d}'.format(hits_7_1))
    hits_1_2 = trees_hit(1, 2)
    print('Trees hit for right 1, down 2: {:d}'.format(hits_1_2))

    print('Multiplied: {:d}'.format(hits_1_1 * hits_3_1 * hits_5_1 * hits_7_1 * hits_1_2))


if __name__ == "__main__":
    part1()
    part2()
