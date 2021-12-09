import time

with open("../input/day09.txt", "r") as fp:
    heightmap = [list(int(i) for i in line.rstrip()) for line in fp.readlines()]


def with_perf_timing(fn):
    start_time = time.perf_counter()
    fn()
    end_time = time.perf_counter()
    print(f'Execution time: {end_time - start_time:0.6f}')


def adjacent_to(row_idx, col_idx, grid):
    neighbors = []
    for r in [row_idx - 1, row_idx, row_idx + 1]:
        if r < 0 or r >= len(grid):
            continue
        for c in [col_idx - 1, col_idx, col_idx + 1]:
            if (c < 0 or c >= len(grid[row_idx])
                    or (r == row_idx and c == col_idx)):
                continue
            neighbors.append(grid[r][c])

    return neighbors


def part1():
    low_points = []
    for row_idx, row in enumerate(heightmap):
        for col_idx, col in enumerate(row):
            adjacents = adjacent_to(row_idx, col_idx, heightmap)
            if col < min(adjacents):
                low_points.append(col)

    total = sum(low_points) + len(low_points)
    print(f'sum of low points with increments of 1 is: {total}')
    return


if __name__ == "__main__":
    with_perf_timing(part1)
    #
    # with_perf_timing(part2)
    #
