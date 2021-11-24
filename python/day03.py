file = open('../input/day03.txt', 'r')
lines = file.readlines()


def inc_x(x, step_x, line_len):
    next_x = x + step_x
    if next_x >= line_len:
        next_x -= line_len

    return next_x


def is_tree(x, line):
    return line[x] == '#'


def part1():
    x = 0
    step_x = 3
    trees_hit = 0

    for line in lines:
        line = line.replace('\n', '')
        trees_hit += 1 if is_tree(x, line) else 0
        x = inc_x(x, step_x, len(line))

    print('Trees hit: {:d}'.format(trees_hit))


if __name__ == "__main__":
    part1()
