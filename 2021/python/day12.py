import time
from copy import deepcopy
from collections import defaultdict

with open("../input/day12.txt", "r") as fp:
    lines = [line.rstrip() for line in fp.readlines()]


def with_perf_timing(fn, args=None):
    start_time = time.perf_counter()
    if args:
        fn(args)
    else:
        fn()
    end_time = time.perf_counter()
    print(f'Execution time: {end_time - start_time:0.6f}')


def initialize_node(node):
    return {'connections': set(),
            'visited': False,
            'multiple_visits_allowed': all(c.isupper() for c in node)}


def to_nodes(data):
    nodes = dict()
    for line in data:
        node1, node2 = line.split('-')
        if node1 not in nodes:
            nodes[node1] = initialize_node(node1)
        if node2 not in nodes:
            nodes[node2] = initialize_node(node2)
        nodes[node1]['connections'].add(node2)
        nodes[node2]['connections'].add(node1)
    return nodes


def explore_path(paths, path, current_node_key, nodes):
    print(f'exploring {path}, stepping on {current_node_key}')
    if current_node_key == 'start':
        print(f'cannot step on start: returning to {path[-1]}')
        return

    if current_node_key == 'end':
        ended_path = deepcopy(path)
        ended_path.append(current_node_key)
        print(f'PATH ENDS: {ended_path}')
        paths.append(ended_path)
        last_node_key = path[-1]
        if not nodes[last_node_key]['multiple_visits_allowed']:
            print(f'{last_node_key} does not allow returns, removing it')
            path.pop()
        return

    current_node = nodes[current_node_key]
    if current_node['visited'] and not current_node['multiple_visits_allowed']:
        last_node_key = path[-1]
        print(f'path terminates: {current_node_key} has been visited and does not allow returns')
        if not nodes[last_node_key]['multiple_visits_allowed']:
            print(f'{last_node_key} does not allow returns, removing it')
            path.pop()
        return
    else:
        path.append(current_node_key)
        print(f'path continues: {current_node_key} is connected to {current_node["connections"]}')
        current_node['visited'] = True
        for next_node_key in current_node['connections']:
            explore_path(paths, path, next_node_key, nodes)
    return


def find_paths_for_network(network):
    nodes = to_nodes(network)
    start_node = nodes['start']
    start_node['multiple_visits_allowed'] = False
    start_node['visited'] = True
    paths = []
    for connected_node_key in start_node['connections']:
        print(f'start -> {connected_node_key}')
        path = ['start']
        explore_path(paths, path, connected_node_key, nodes)
    print(f'\nnetwork: {network}\npaths: {paths}')
    return


def part1():
    # one_path = ['start-end']
    # find_paths_for_network(one_path)
    #
    # straight_path = ['start-a', 'a-end']
    # find_paths_for_network(straight_path)
    #
    # split_path = ['start-a', 'start-b', 'a-end', 'b-end']
    # find_paths_for_network(split_path)
    #
    # unusable_split_path = ['start-a', 'start-b', 'a-end', 'b-end', 'c-a']
    # find_paths_for_network(unusable_split_path)
    #
    # reusable_path = ['start-A', 'A-end', 'c-A']
    # find_paths_for_network(reusable_path)
    # print('should have: [[start, A, end], [start, A, c, A, end]]')
    #
    # usable_split_path = ['start-A', 'start-b', 'A-end', 'b-end', 'c-A']
    # find_paths_for_network(usable_split_path)
    # print('should have: [[start, A, end], [start, b, end], [start, A, c, A, end]]\n')

    simple_cave = ['start-A', 'start-b',
                   'c-A', 'A-b', 'b-d',
                   'A-end', 'b-end']
    # find_paths_for_network(simple_cave)

    return


def dfs(cave, visited, one_off, paths):
    if cave == 'end':
        return 1

    if cave.islower():
        visited.add(cave)

    total = sum([dfs(current_cave, visited, one_off, paths)
                 for current_cave in paths[cave]
                 if current_cave not in visited])
    total += (sum([dfs(visited_cave, visited, visited_cave, paths)
                  for visited_cave in paths[cave]
                  if visited_cave in visited and visited_cave != 'start'])
              if one_off == ' ' else 0)

    if cave != one_off:
        visited.discard(cave)

    return total


def aoc12_mockle2():
    usable_split_path = ['start-A', 'start-b', 'A-end', 'b-end', 'c-A']
    simple_cave = ['start-A', 'start-b',
                   'c-A', 'A-b', 'b-d',
                   'A-end', 'b-end']
    paths = defaultdict(list)
    # for a, b in [line.split('-') for line in simple_cave]:
    for a, b in [line.split('-') for line in open('../input/day12.txt').read().splitlines()]:
        paths[a].append(b)
        paths[b].append(a)

    print('Part 1:', dfs('start', set(), '', paths))
    print('Part 2:', dfs('start', set(), ' ', paths))


def aoc12_jools_jops(filename):
    graph = {
        "start": [],
        "end": []}

    with open(filename, 'r') as f:
        for line in f.readlines():
            a, b = line.strip().split('-')
            if a not in graph.keys():
                graph[a] = []
            graph[a].append(b)
            if b not in graph.keys():
                graph[b] = []
            graph[b].append(a)

    node = 'start'
    path = [0, node]  # path[0] added to track one revisit to small cave
    count = 0
    paths = [path]
    while len(paths) != 0:
        if node.islower() and path.count(node) > 1:  # added for day 12B
            path[0] = 1
        for n in graph[node]:
            if n == 'start':
                continue
            if n == 'end':
                count += 1
                continue
            if n in path and n.islower() and path[0] == 1:  # 'and path[0] == 1' added for day 12B
                continue
            paths.append(path + [n])
        path = paths.pop()
        node = path[-1]

    print(count)


if __name__ == "__main__":
    with_perf_timing(aoc12_mockle2)
    # with_perf_timing(aoc12_jools_jops, '../input/day12.txt')
    # with_perf_timing(part1)
    #
    # with_perf_timing(part2)
    #
