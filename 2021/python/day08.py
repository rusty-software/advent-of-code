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


#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....
#
#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg


def what_a_mess(line):
    digit_segments = [s for s in line.split(' ')][:-5]
    output_values = [set(s) for s in line.split(' ')][-4:]
    one_digital = set([s for s in digit_segments if len(s) == 2][0])
    four_digital = set([s for s in digit_segments if len(s) == 4][0])
    seven_digital = set([s for s in digit_segments if len(s) == 3][0])
    eight_digital = set([s for s in digit_segments if len(s) == 7][0])

    digitals = dict()
    digitals['1'] = one_digital
    digitals['4'] = four_digital
    digitals['7'] = seven_digital
    digitals['8'] = eight_digital

    # difference between the 7 and 1 digits upper segment
    u_segment = list(seven_digital.difference(one_digital))[0]

    # find the 9 by taking the 4, adding the upper segment, and isolating the
    # six-length segment with a single difference
    almost_nine = four_digital.copy()
    almost_nine.add(u_segment)
    l_segment = ''
    ll_segment = ''
    six_len_segments = [set(s) for s in digit_segments if len(s) == 6]
    for segment in six_len_segments:
        d = segment.difference(almost_nine)
        if len(d) == 1:
            digitals['9'] = segment
            # difference between (4 and upper) and 9 digit is lower segment
            l_segment = list(d)[0]
            # extra bonus: difference between the 8 and 9 digits lower left segment
            ll_segment = list(eight_digital.difference(segment))[0]

    # find the 3 by taking the one, adding the upper and lower segments, and
    # isolating the five-length segment with a single difference
    almost_three = one_digital.copy()
    almost_three.update([u_segment, l_segment])
    five_len_segments = [set(s) for s in digit_segments if len(s) == 5]
    m_segment = ''
    for segment in five_len_segments:
        d = segment.difference(almost_three)
        if len(d) == 1:
            digitals['3'] = segment
            # difference between (1 and upper and lower) and 3 digit is middle segment
            m_segment = list(d)[0]

    # find the 0 by taking the one, adding upper, lower, and lower left
    # segments, and isolating the six-length segment with a single difference.
    # The remaining six-length segment is the 6.
    almost_zero = one_digital.copy()
    almost_zero.update([u_segment, l_segment, ll_segment])
    ul_segment = ''
    for segment in six_len_segments:
        if segment in digitals.values():
            continue

        d = segment.difference(almost_zero)
        if len(d) == 1:
            digitals['0'] = segment
            # difference between nearly zero and 0 is the upper left segment
            ul_segment = list(d)[0]
        else:
            digitals['6'] = segment

    # find the 5 by combining an upper, upper left, middle, and lower segment,
    # then isolating the five-length segment with a single difference. The
    # remaining five-length segment is the 2.
    almost_five = {u_segment, ul_segment, m_segment, l_segment}
    for segment in five_len_segments:
        if segment in digitals.values():
            continue

        d = segment.difference(almost_five)
        if len(d) == 1:
            digitals['5'] = segment
        else:
            digitals['2'] = segment

    num = ''
    for output_value in output_values:
        num += [k for k, v in digitals.items() if v == output_value][0]

    return num


def part2():
    output_num_sum = 0
    for line in lines:
        output_num_sum += int(what_a_mess(line))

    print(f'line output num sum: {output_num_sum}')
    return


if __name__ == "__main__":
    # with_perf_timing(part1)
    # 534
    with_perf_timing(part2)
    # 1070188
