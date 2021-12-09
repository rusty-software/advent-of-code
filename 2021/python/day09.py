import time

with open("../input/day09_sample.txt", "r") as fp:
    heightmap = [list(int(i) for i in line.rstrip()) for line in fp.readlines()]


def with_perf_timing(fn):
    start_time = time.perf_counter()
    fn()
    end_time = time.perf_counter()
    print(f'Execution time: {end_time - start_time:0.6f}')


def adjacent_to(row_idx, col_idx, grid):
    adjacent_points = []
    for r in [row_idx - 1, row_idx, row_idx + 1]:
        if r < 0 or r >= len(grid):
            continue
        for c in [col_idx - 1, col_idx, col_idx + 1]:
            if (c < 0 or c >= len(grid[row_idx])
                    or (r == row_idx and c == col_idx)):
                continue
            adjacent_points.append(grid[r][c])

    return adjacent_points


def low_points(grid):
    lows = dict()
    for row_idx, row in enumerate(grid):
        for col_idx, col in enumerate(row):
            adjacent_points = adjacent_to(row_idx, col_idx, grid)
            if col < min(adjacent_points):
                lows[(row_idx, col_idx)] = col
    return lows


def part1():
    lows = low_points(heightmap)
    total = sum(lows.values()) + len(lows)
    print(f'sum of low points with increments of 1 is: {total}')
    return


def basin_for(point, grid):
    basin = []
    point_x = point[0]
    point_y = point[1]
    point_val = grid[point_x][point_y]

    print(f'grid[{point_x}][{point_y}] is {point_val} and has adjacencies {adjacent_to(point_x, point_y, grid)}')
    return basin


def part2():
    lows = low_points(heightmap)
    basins = []
    for low_point, low in lows.items():
        basin = basin_for(low_point, heightmap)
        # print(f'{low} at {low_point} surrounded by {basin}')
    return


if __name__ == "__main__":
    # with_perf_timing(part1)
    # 532
    with_perf_timing(part2)
    #
