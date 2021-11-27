import copy

with open("../input/day11.txt", "r") as fp:
    initial_seats = [list(line.rstrip()) for line in fp.readlines()]


def seats_adjacent_to(row_idx, seat_idx, seats):
    neighbors = []
    for r in [row_idx - 1, row_idx, row_idx + 1]:
        if r < 0 or r >= len(seats):
            continue
        for s in [seat_idx - 1, seat_idx, seat_idx + 1]:
            if s < 0 or s >= len(seats[row_idx]) \
                    or (r == row_idx and s == seat_idx):
                continue
            neighbors.append(seats[r][s])

    return neighbors


def part1():
    seats = []
    evolved_seats = initial_seats.copy()

    while seats != evolved_seats:
        seats = copy.deepcopy(evolved_seats)
        for row_idx, seat_row in enumerate(seats):
            for seat_idx, seat in enumerate(seat_row):
                adjacent_seats = seats_adjacent_to(row_idx, seat_idx, seats)
                if seat == 'L' and '#' not in adjacent_seats:
                    evolved_seats[row_idx][seat_idx] = '#'
                elif seat == '#' and len([s for s in adjacent_seats if s == '#']) >= 4:
                    evolved_seats[row_idx][seat_idx] = 'L'
                else:
                    evolved_seats[row_idx][seat_idx] = seat

        occupied_seats_sum = 0
        for row in evolved_seats:
            occupied_seats_sum += sum([len(s) for s in row if s == '#'])
            print(''.join(row))

        print(f'occupied seats sum: {occupied_seats_sum}')

    return


if __name__ == "__main__":
    part1()
    # 2222
    # part2()
    # ?
