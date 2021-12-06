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


def organized_population_growth(initial_population, days, reproduction_frequency):
    current_population = initial_population.copy()

    population_age_counts = dict()
    for age_key in range(reproduction_frequency + 2):
        population_age_counts[age_key] = 0

    for age in current_population:
        population_age_counts[age] += 1

    for day in range(days):
        working = population_age_counts.copy()

        for age_key, age_count in working.items():
            if age_key == 0:
                population_age_counts[reproduction_frequency + 1] = age_count
                population_age_counts[reproduction_frequency - 1] = age_count + working[reproduction_frequency]
            elif age_key == reproduction_frequency:
                continue
            else:
                population_age_counts[age_key - 1] = working[age_key]

    return population_age_counts


def part1():
    initial_population = line
    grown_population = population_growth(initial_population, 80)
    print(f'population count after 80 days: {len(grown_population)}')

    return


def part2():
    initial_population = line
    grown_population = organized_population_growth(initial_population, 256, 7)
    print(f'population count after 256 days: {sum(grown_population.values())}')

    return


if __name__ == "__main__":
    with_perf_timing(part1)
    # 372984
    with_perf_timing(part2)
    # 1681503251694
