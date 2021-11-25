import re

with open('../input/day07.txt', 'r') as f:
    lines = f.readlines()
lines = [line.split("\n")[0] for line in lines]


def bag_desc(bag):
    # removes numbers, periods, and the literals 'bags' and 'bag'. Also trims.
    return re.sub(r'\d|\.|bags|bag', '', bag).strip()


def bag_list(contents):
    bags = list(map(bag_desc, contents.split(',')))
    return bags


def find_parents(acc, current_bag, bag_to_parents):
    acc.add(current_bag)
    if current_bag in bag_to_parents.keys():
        for parent_bag in bag_to_parents[current_bag]:
            find_parents(acc, parent_bag, bag_to_parents)
    return


def part1():
    my_bag = 'shiny gold'
    parent_of_none = 'no other'
    all_possible_parents = set()

    bag_to_parents = {}
    for line in lines:
        outer_bag, contents = line.split('contain')
        outer_bag = bag_desc(outer_bag)
        contained_bags = bag_list(contents)
        if parent_of_none not in contained_bags:
            for bag in contained_bags:
                if bag in bag_to_parents.keys():
                    bag_to_parents[bag].add(outer_bag)
                else:
                    bag_to_parents[bag] = {outer_bag}

    find_parents(all_possible_parents, my_bag, bag_to_parents)

    # set includes my bag, so don't count it
    print(len(all_possible_parents) - 1)
    return


def part2():
    return


if __name__ == "__main__":
    part1()
    # 274
    part2()
    # ?
