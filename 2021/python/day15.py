import time

with open("../input/day15_sample.txt", "r") as fp:
    file_data = [list(int(i) for i in line.rstrip()) for line in fp.readlines()]


def with_perf_timing(fn, args=None):
    start_time = time.perf_counter()
    if args:
        fn(args)
    else:
        fn()
    end_time = time.perf_counter()
    print(f'Execution time: {end_time - start_time:0.6f}')


def part1():
    print(file_data)
    return


if __name__ == "__main__":
    with_perf_timing(part1)
    #
    # with_perf_timing(part2)
    #
