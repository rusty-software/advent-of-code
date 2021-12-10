import time
from collections import deque

with open("../input/day10.txt", "r") as fp:
    lines = [list(i for i in line.rstrip()) for line in fp.readlines()]


def with_perf_timing(fn):
    start_time = time.perf_counter()
    fn()
    end_time = time.perf_counter()
    print(f'Execution time: {end_time - start_time:0.6f}')


openers = ['(', '[', '{', '<']

pairs = {'(': ')',
         '[': ']',
         '{': '}',
         '<': '>'}

point_values = {')': 3,
                ']': 57,
                '}': 1197,
                '>': 25137}


def part1():
    error_score = 0
    for line in lines:
        stack = deque()
        for c in line[:-1]:
            if c in openers:
                stack.append(c)
            else:
                last_open = stack.pop()
                if c != pairs[last_open]:
                    error_score += point_values[c]

    print(f'Error score: {error_score}')
    return


if __name__ == "__main__":
    with_perf_timing(part1)
    #
    # with_perf_timing(part2)
    #
