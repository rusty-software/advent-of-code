import time

with open("../input/day14_sample.txt", "r") as fp:
    file_data = [line.rstrip() for line in fp.readlines()]


def with_perf_timing(fn, args=None):
    start_time = time.perf_counter()
    if args:
        fn(args)
    else:
        fn()
    end_time = time.perf_counter()
    print(f'Execution time: {end_time - start_time:0.6f}')


def to_template_rules(data):
    return data[0], data[2:]


def to_rules(unparsed_rules):
    rules = dict()
    for pair, product in [r.split(' -> ') for r in unparsed_rules]:
        rules[(pair[0], pair[1])] = product
    return rules


def part1():
    template, unparsed_rules = to_template_rules(file_data)
    rules = to_rules(unparsed_rules)
    print(rules)

    return


if __name__ == "__main__":
    with_perf_timing(part1)
    #
    # with_perf_timing(part2)
    #
