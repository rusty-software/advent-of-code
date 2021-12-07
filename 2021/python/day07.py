import time

with open("../input/day07.txt", "r") as fp:
    positions = [int(num) for num in [line.rstrip() for line in fp.readlines()][0].split(',')]


def with_perf_timing(fn):
    start_time = time.perf_counter()
    fn()
    end_time = time.perf_counter()
    print(f'Execution time: {end_time - start_time:0.6f}')


def part1():
    return


def part2():
    return


if __name__ == "__main__":
    with_perf_timing(part1)
    #
    with_perf_timing(part2)
    #
