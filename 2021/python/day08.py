import time

with open("../input/day08_sample.txt", "r") as fp:
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
    known_len_to_digit = dict()
    known_len_to_digit[2] = '1'
    known_len_to_digit[3] = '7'
    known_len_to_digit[4] = '4'
    known_len_to_digit[7] = '8'

    line = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'
    scrambled_digits = [s for s in line.split(' ')]

    return


# for line in lines:
#     outputs = [s for s in line.split(' ')[-4:]]
#     print(outputs)
#     digits = ''
#     for output in outputs:
#         if len(output) in known_len_to_digit:
#             digits += known_len_to_digit[len(output)]
#         else:
#             digits += '?'
#
#     print(f'digits: {digits}')


if __name__ == "__main__":
    with_perf_timing(part1)
    # 534
    with_perf_timing(part2)
    #
