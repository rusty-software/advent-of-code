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
    digit_positions = {0: {'u', 'ul', 'ur', 'll', 'lr', 'l'},
                       1: {'ur', 'lr'},
                       2: {'u', 'ur', 'm', 'll', 'l'},
                       3: {'u', 'ur', 'm', 'lr', 'l'},
                       4: {'ul', 'ur', 'm', 'lr'},
                       5: {'u', 'ul', 'm', 'lr', 'l'},
                       6: {'u', 'ul', 'm', 'll', 'lr', 'l'},
                       7: {'u', 'ur', 'lr'},
                       8: {'u', 'ul', 'ur', 'm', 'll', 'lr', 'l'},
                       9: {'u', 'ul', 'ur', 'm', 'lr', 'l'}}

    segment_position = dict()
    for segment in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        segment_position[segment] = {'positions': set(),
                                     'cur_length': 0}

    line = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'
    print(line)

    digit_segments = [s for s in line.split(' ')][:-5]
    # output_values = [s for s in line.split(' ')][-4:]
    for digit_segment in digit_segments:
        segment_len = len(digit_segment)
        if segment_len == 2:
            for segment in digit_segment:
                if len(segment_position[segment]) != 1:
                    segment_position[segment] = digit_positions[1].copy()
        elif segment_len == 3:
            for segment in digit_segment:
                if len(segment_position[segment]) != 1:
                    segment_position[segment] = digit_positions[7].copy()
        # elif segment_len == 4:
        #     for segment in digit_segment:
        #         segment_position[segment] = digit_positions[4].copy()
        # elif segment_len == 7:
        #     for segment in digit_segment:
        #         segment_position[segment] = digit_positions[8].copy()
    print(f'segment position: {segment_position}')

    for segment, positions in segment_position.items():

    return


if __name__ == "__main__":
    # with_perf_timing(part1)
    # 534
    with_perf_timing(part2)
    #
