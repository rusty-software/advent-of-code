import re

with open('../input/day07.txt', 'r') as f:
    lines = f.readlines()
lines = [line.split("\n")[0] for line in lines]


def bag_desc(bag):
    # removes numbers, periods, and the literals 'bags' and 'bag'. Also trims.
    return re.sub(r'\d|\.|bags|bag', '', bag).strip()


def bags_from(contents):
    bags = list(map(bag_desc, contents.split(',')))
    return bags


def bags_quantities_from(contents):
    bags_quantities = {}
    contains_none = 'no other'
    for raw_bag in contents.split(','):
        raw_bag = re.sub(r'\.|bags|bag', '', raw_bag).strip()
        if raw_bag == contains_none:
            continue
        quantity_bag = raw_bag.split(' ')
        quantity = int(quantity_bag.pop(0))
        bag = ' '.join(quantity_bag)
        bags_quantities[bag] = quantity
    return bags_quantities


def find_parents(acc, current_bag, bag_to_parents):
    acc.add(current_bag)
    if current_bag in bag_to_parents.keys():
        for parent_bag in bag_to_parents[current_bag]:
            find_parents(acc, parent_bag, bag_to_parents)
    return


def sum_children(acc, current_bag, bag_contents):
    print(f'acc: {acc}, current_bag: {current_bag}')
    if bag_contents.get(current_bag) is not None:
        children = bag_contents.get(current_bag)
        if children:
            print(f'continuing with: {children}')
            for child_bag_key in children:
                print(f'acc {acc} will become {acc["count"] + children.get(child_bag_key)} because {child_bag_key}')
                acc['count'] += children.get(child_bag_key)
                sum_children(acc, child_bag_key, bag_contents)
    return acc


def part1():
    my_bag = 'shiny gold'
    parent_of_none = 'no other'
    all_possible_parents = set()

    bag_to_parents = {}
    for line in lines:
        outer_bag, contents = line.split('contain')
        outer_bag = bag_desc(outer_bag)
        contained_bags = bags_from(contents)
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
    my_bag = 'shiny gold'
    # my_bag = 'wavy bronze'

    bag_contents = {}
    for line in lines:
        outer_bag, contents = line.split('contain')
        outer_bag = bag_desc(outer_bag)
        contained_bags_quantities = bags_quantities_from(contents)
        bag_contents[outer_bag] = contained_bags_quantities

    sum_quantities = {'count': 0}
    sum_children(sum_quantities, my_bag, bag_contents)
    print(sum_quantities)
    return


test_bags = {"shiny gold": {"dark red": 2},
             "dark red": {"dark orange": 2},
             "dark orange": {"dark yellow": 2},
             "dark yellow": {"dark green": 2},
             "dark green": {"dark blue": 2},
             "dark blue": {"dark violet": 2},
             "dark violet": 0}

# solution from https://dev.to/qviper/advent-of-code-2020-python-solution-day-7-5319
with open("../input/day07.txt", "r") as fp:
    lines = fp.readlines()
    lines = [line.rstrip() for line in lines]

# to make a dictionary of bags
bag_types = []
all_bags = {}
for line in lines:
    mbag = " ".join(line.split(" ")[:2])
    contains = line[line.index("contain ") + 8:-1]
    each_contain = contains.split(",")
    each_contain = [cnt.lstrip() for cnt in each_contain]
    each_contain = [" ".join(cont.split(" ")[:-1]) for cont in each_contain]
    # print(each_contain)
    each_contain = {" ".join(cont.split(" ")[1:]): cont.split(" ")[0] for cont in each_contain}
    # print(each_contain)
    if mbag not in bag_types:
        bag_types.append(mbag)
    if all_bags.get(mbag):
        each_contain.update(all_bags[mbag])
    all_bags[mbag] = each_contain

my_bag = "shiny gold"
bags_contains = {}
test_bags = all_bags
for k, v in test_bags.items():
    bags_contains[k] = []
    try:
        for kk, vv in v.items():
            bags_contains[k] += [kk] * int(vv)
    except:
        pass


def count_bags(current_bag):
    if current_bag == " " or bags_contains.get(current_bag) is None:
        return 0

    # print("key:", current_bag)
    cnt = len(bags_contains[current_bag])
    cnts = []
    for k in bags_contains[current_bag]:
        cnts.append(count_bags(k))
    return sum(cnts) + cnt


if __name__ == "__main__":
    # part1()
    # 274
    # part2()
    # ?
    print(f"{my_bag} bag can hold {count_bags('shiny gold')} bags")
