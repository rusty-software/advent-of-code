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

corruption_point_values = {')': 3,
                           ']': 57,
                           '}': 1197,
                           '>': 25137}


def corruption(line):
    stack = deque()
    for c in line[:-1]:
        if c in openers:
            stack.append(c)
        else:
            last_open = stack.pop()
            if c != pairs[last_open]:
                return c

    return None


def part1():
    error_score = 0
    for line in lines:
        c = corruption(line)
        if c:
            error_score += corruption_point_values[c]

    print(f'Error score: {error_score}')
    return


def completion(line):
    open_stack = deque()
    for c in line:
        if c in openers:
            open_stack.append(c)
        else:
            open_stack.pop()

    open_stack = list(open_stack)
    open_stack.reverse()
    completions = []
    for c in open_stack:
        completions.append(pairs[c])

    return completions


completion_point_values = {')': 1,
                           ']': 2,
                           '}': 3,
                           '>': 4}


def part2():
    incomplete_lines = [line for line in lines if not corruption(line)]
    completion_scores = []
    for line in incomplete_lines:
        missing_closers = completion(line)
        completion_score = 0
        for missing_closer in missing_closers:
            completion_score = (completion_score * 5) + completion_point_values[missing_closer]

        completion_scores.append(completion_score)

    completion_scores.sort()
    print(f'Middle score: {completion_scores[len(completion_scores) // 2]}, from {completion_scores}')
    return


if __name__ == "__main__":
    # with_perf_timing(part1)
    # 193275
    with_perf_timing(part2)
    # 2429644557
