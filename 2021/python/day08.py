import time

with open("../input/day08.txt", "r") as fp:
    lines = [line.rstrip() for line in fp.readlines()]


def with_perf_timing(fn):
    start_time = time.perf_counter()
    fn()
    end_time = time.perf_counter()
    print(f'Execution time: {end_time - start_time:0.6f}')


def part1():
    total = 0
    for line in lines:
        digit_lengths = [len(s) for s in line.split(' ')[-4:]]
        total += len([v for v in digit_lengths if v in [2, 3, 4, 7]])

    print(f'total: {total}')
    return


def part2():
    return


if __name__ == "__main__":
    with_perf_timing(part1)
    #
    with_perf_timing(part2)
    #
