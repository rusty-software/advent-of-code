import time

with open("../input/day11.txt", "r") as fp:
    file_data = [list(int(i) for i in line.rstrip()) for line in fp.readlines()]


def with_perf_timing(fn):
    start_time = time.perf_counter()
    fn()
    end_time = time.perf_counter()
    print(f'Execution time: {end_time - start_time:0.6f}')


def reset_energy_levels(octopuses):
    for row_idx, _ in enumerate(octopuses):
        for col_idx, v in enumerate(octopuses[row_idx]):
            if v > 9:
                octopuses[row_idx][col_idx] = 0
    return


def neighbors_for(row_idx, col_idx, grid):
    neighbors = []
    for r in [row_idx - 1, row_idx, row_idx + 1]:
        if 0 <= r < len(grid):
            for c in [col_idx - 1, col_idx, col_idx + 1]:
                if (0 <= c < len(grid[r])
                        and not (r == row_idx and c == col_idx)):
                    neighbors.append((r, c))
    return neighbors


def initialize_octopuses(grid):
    octopuses = dict()
    for row_idx, row in enumerate(grid):
        for col_idx, col_val in enumerate(row):
            octopuses[(row_idx, col_idx)] = {'energy_level': col_val,
                                             'neighbors': neighbors_for(row_idx, col_idx, grid)}
    return octopuses


def initial_energizing(octopuses):
    energized_octopuses = []
    for octopus_point, octopus_data in octopuses.items():
        octopus_data['energy_level'] += 1
        if octopus_data['energy_level'] > 9:
            energized_octopuses.append(octopus_point)
    return energized_octopuses


def energize_neighbors(energized_octopus_point, octopuses, energized_stats):
    energized_stats['flash_total'] += 1
    for neighbor_point in octopuses[energized_octopus_point]['neighbors']:
        energy_level = octopuses[neighbor_point]['energy_level']
        if energy_level <= 9:
            octopuses[neighbor_point]['energy_level'] += 1
            if octopuses[neighbor_point]['energy_level'] > 9:
                energize_neighbors(neighbor_point, octopuses, energized_stats)
    return


def reset_flashed(octopuses):
    for octopus_point, octopus_data in octopuses.items():
        if octopus_data['energy_level'] > 9:
            octopus_data['energy_level'] = 0
    return


def energize(energized_stats, octopuses):
    energized_octopus_points = initial_energizing(octopuses)
    for energized_octopus_point in energized_octopus_points:
        energize_neighbors(energized_octopus_point, octopuses, energized_stats)
    reset_flashed(octopuses)


def part1():
    # fixed = [[1, 1, 1, 1, 1],
    #          [1, 9, 9, 9, 1],
    #          [1, 9, 1, 9, 1],
    #          [1, 9, 9, 9, 1],
    #          [1, 1, 1, 1, 1]]

    octopuses = initialize_octopuses(file_data)
    energized_stats = {'flash_total': 0}
    for i in range(100):
        energize(energized_stats, octopuses)
    print(energized_stats)

    return


if __name__ == "__main__":
    with_perf_timing(part1)
    #
    # with_perf_timing(part2)
    #
