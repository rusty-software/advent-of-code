import time
from collections import Counter
from copy import deepcopy
from pprint import pprint

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


def grow_by_iteration(iteration_count):
    polymer, unparsed_rules = to_template_rules(file_data)
    rules = to_rules(unparsed_rules)

    for i in range(iteration_count):
        polymer = grow(polymer, rules)
    frequency = Counter(polymer)
    most = max(frequency, key=frequency.get)
    most_count = frequency.get(most)
    least = min(frequency, key=frequency.get)
    least_count = frequency.get(least)
    print(f'{most}: {most_count} - {least}: {least_count} = {most_count - least_count}')
    return


def part1():
    grow_by_iteration(10)


def to_pair_data(unparsed_rules):
    rules = dict()
    for pair, product in [r.split(' -> ') for r in unparsed_rules]:
        rules[pair] = {'product': product, 'count': 0}
    return rules


def initialize_pair_count(pairs, polymer):
    for idx, element in enumerate(polymer):
        if idx == len(polymer) - 1:
            break
        pairs[f'{element}{polymer[idx + 1]}']['count'] += 1
    return


def initialize_product_count(product_count, pairs, polymer):
    for pair, pair_data in pairs.items():
        product = pair_data['product']
        if product not in product_count:
            product_count[product] = 0

    for element in polymer:
        product_count[element] += 1
    return


def part2():
    # apparently, brute force won't scale to 40
    polymer, unparsed_rules = to_template_rules(file_data)
    pairs = to_pair_data(unparsed_rules)
    initialize_pair_count(pairs, polymer)
    product_counts = dict()
    initialize_product_count(product_counts, pairs, polymer)

    working_pairs = deepcopy(pairs)
    for i in range(40):
        for pair, pair_data in working_pairs.items():
            pair_count = pair_data['count']
            if pair_count > 0:
                product = pair_data['product']
                left_pair = f'{pair[0]}{product}'
                right_pair = f'{product}{pair[1]}'
                pairs[left_pair]['count'] += pair_count
                pairs[right_pair]['count'] += pair_count
                pairs[pair]['count'] -= pair_count
                product_counts[product] += pair_count
        working_pairs = deepcopy(pairs)
    pprint(pairs)
    pprint(product_counts)
    max_count = max([c for c in product_counts.values()])
    min_count = min([c for c in product_counts.values()])
    print(max_count - min_count)
    return


if __name__ == "__main__":
    # with_perf_timing(part1)
    # 2549
    with_perf_timing(part2)
    # 2516901104210
