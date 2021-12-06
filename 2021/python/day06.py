import time

with open("../input/day06.txt", "r") as fp:
    line = [int(num) for num in [line.rstrip() for line in fp.readlines()][0].split(',')]


def with_perf_timing(fn):
    start_time = time.perf_counter()
    fn()
    end_time = time.perf_counter()
    print(f'Execution time: {end_time - start_time:0.6f}')


def population_growth(initial_population, days):
    current_population = initial_population.copy()
    for day in range(days):
        for idx, _ in enumerate(current_population):
            current_population[idx] -= 1
            if current_population[idx] < 0:
                current_population[idx] = 6
                current_population.append(9)
    return current_population


def part1():
    initial_population = line
    grown_population = population_growth(initial_population, 80)
    print(f'population count after 80 days: {len(grown_population)}')

    return


def part2():
    initial_population = line
    grown_population = population_growth(initial_population, 256)
    print(f'population count after 256 days: {len(grown_population)}')

    return


if __name__ == "__main__":
    # with_perf_timing(part1)
    # 372984
    with_perf_timing(part2)
    #
