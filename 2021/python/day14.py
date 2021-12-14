import time
from collections import Counter

with open("../input/day14.txt", "r") as fp:
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


def grow(polymer, rules):
    polymer_pairs = []
    for idx, element in enumerate(polymer):
        if idx == len(polymer) - 1:
            break
        polymer_pairs.append([element, polymer[idx + 1]])

    grown_polymer = [polymer[0]]
    for left, right in polymer_pairs:
        grown_polymer.append(rules[(left, right)])
        grown_polymer.append(right)

    return ''.join(grown_polymer)


def part1():
    polymer, unparsed_rules = to_template_rules(file_data)
    rules = to_rules(unparsed_rules)

    for i in range(10):
        polymer = grow(polymer, rules)
    frequency = Counter(polymer)
    most = max(frequency, key=frequency.get)
    most_count = frequency.get(most)
    least = min(frequency, key=frequency.get)
    least_count = frequency.get(least)
    print(f'{most}: {most_count} - {least}: {least_count} = {most_count - least_count}')
    return


if __name__ == "__main__":
    with_perf_timing(part1)
    # 2549
    # with_perf_timing(part2)
    #
