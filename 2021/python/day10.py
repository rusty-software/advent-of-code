import time
from collections import deque
from pprint import pprint

with open("../input/day10_sample.txt", "r") as fp:
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
    complete_lines = [line for line in lines if len(line) % 2 == 0]

    for line in complete_lines:
        stack = deque()
        for c in line:
            if c in openers:
                stack.append(c)
            else:
                last_open = stack.pop()
                if c != pairs[last_open]:
                    print(f'found a mismatch: {last_open}, {c}')
    return


if __name__ == "__main__":
    with_perf_timing(part1)
    #
    # with_perf_timing(part2)
    #
