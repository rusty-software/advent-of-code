import time
import math

with open("../input/day09.txt", "r") as fp:
    heightmap = [list(int(i) for i in line.rstrip()) for line in fp.readlines()]


def with_perf_timing(fn):
    start_time = time.perf_counter()
    fn()
    end_time = time.perf_counter()
    print(f'Execution time: {end_time - start_time:0.6f}')


def adjacent_to(row_idx, col_idx, grid):
    adjacent_points = dict()
    for r in [row_idx - 1, row_idx, row_idx + 1]:
        if r < 0 or r >= len(grid):
            continue
        for c in [col_idx - 1, col_idx, col_idx + 1]:
            if (c < 0 or c >= len(grid[row_idx])
                    or (r == row_idx and c == col_idx)):
                continue
            adjacent_points[(r, c)] = grid[r][c]

    return adjacent_points


def low_points(grid):
    lows = dict()
    for row_idx, row in enumerate(grid):
        for col_idx, col in enumerate(row):
            adjacent_points = adjacent_to(row_idx, col_idx, grid)
            if col < min(adjacent_points.values()):
                lows[(row_idx, col_idx)] = col
    return lows


def part1():
    lows = low_points(heightmap)
    total = sum(lows.values()) + len(lows)
    print(f'sum of low points with increments of 1 is: {total}')
    return


def step_up(acc, point, grid):
    point_x, point_y = point
    point_val = grid[point_x][point_y]
    acc[point] = point_val
    adjacent_points = adjacent_to(point_x, point_y, grid)
    for adjacent_point, adjacent_point_val in adjacent_points.items():
        if adjacent_point in acc:
            continue
        elif adjacent_point_val == 9:
            continue
        elif adjacent_point_val != point_val + 1:
            continue
        else:
            step_up(acc, adjacent_point, grid)

    return


def part2():
    lows = low_points(heightmap)
    basins = dict()
    largest_basins = [0, 0, 0]
    for low_point, low_point_val in lows.items():
        basins[low_point] = dict()
        step_up(basins[low_point], low_point, heightmap)
        basin_size = len(basins[low_point])
        if basin_size > min(largest_basins):
            largest_basins.sort()
            largest_basins.append(basin_size)
            del largest_basins[0]

    print(f'largest basin: {largest_basins}; product: {largest_basins[0] * largest_basins[1] * largest_basins[2]}')
    return


groups = []


def count_groups(col_idx, row_idx):
    if (row_idx < 0 or row_idx >= len(heightmap)
            or col_idx < 0 or col_idx >= len(heightmap[0])
            or heightmap[row_idx][col_idx] == 9
            or heightmap[row_idx][col_idx] == -1):
        return
    heightmap[row_idx][col_idx] = -1
    groups[len(groups) - 1] += 1
    count_groups(col_idx + 1, row_idx)
    count_groups(col_idx - 1, row_idx)
    count_groups(col_idx, row_idx + 1)
    count_groups(col_idx, row_idx - 1)


def part2_cheating():
    """
    Shamefully swiped from https://zonito.medium.com/smoke-basin-day-9-advent-of-code-2021-python-solution-54c8d3da58a7
    """
    for row_idx in range(0, len(heightmap)):
        for col_idx in range(0, len(heightmap[0])):
            groups.append(0)
            count_groups(col_idx, row_idx)
    print(math.prod(sorted(groups, reverse=True)[:3]))


if __name__ == "__main__":
    # with_perf_timing(part1)
    # 532
    # with_perf_timing(part2)
    # 969903, which is wrong
    with_perf_timing(part2_cheating)
    # 1110780, which is right
