with open("../input/day12.txt", "r") as fp:
    instructions = [line.rstrip() for line in fp.readlines()]

sample_instructions = [
    'F10'
    , 'N3'
    , 'F7'
    , 'R90'
    , 'F11'
]


cardinal_directions = ['E', 'S', 'W', 'N']


def rotate(current_direction, turn, degrees):
    rotation_rate = int(degrees / 90)
    current_direction_idx = cardinal_directions.index(current_direction)
    if turn == 'R':
        next_direction_idx = current_direction_idx + rotation_rate
        if next_direction_idx >= len(cardinal_directions):
            next_direction_idx -= len(cardinal_directions)
    else:
        next_direction_idx = current_direction_idx - rotation_rate
        if next_direction_idx < 0:
            next_direction_idx += len(cardinal_directions)

    return cardinal_directions[next_direction_idx]


def move(position, direction, distance):
    if direction == 'N':
        position[0] += distance
    if direction == 'S':
        position[0] -= distance
    if direction == 'E':
        position[1] += distance
    if direction == 'W':
        position[1] -= distance

    return


def part1():
    position = [0, 0]
    current_direction = 'E'

    for idx, instruction in enumerate(instructions):
        direction, distance = [instruction[0], int(instruction[1:])]
        print(f'instruction idx: {idx}, direction: {direction}, distance: {distance}')
        if direction in ['R', 'L']:
            current_direction = rotate(current_direction, direction, distance)
        elif direction == 'F':
            move(position, current_direction, distance)
        else:
            move(position, direction, distance)

    print(f'manhattan distance: {abs(position[0]) + abs(position[1])}')
    return


def rotate_waypoint(waypoint_current_direction, directive, degrees):
    for idx, cardinal_direction in enumerate(waypoint_current_direction):
        waypoint_current_direction[idx] = rotate(cardinal_direction, directive, degrees)
    return


def advance_ship(ship_position, waypoint_relative_position, waypoint_current_direction, distance):
    if waypoint_current_direction[0] == 'E':
        ship_position[0] = ship_position[0] + (waypoint_relative_position[0] * distance)
    if waypoint_current_direction[1] == 'E':
        ship_position[0] = ship_position[0] + (waypoint_relative_position[1] * distance)
    if waypoint_current_direction[0] == 'W':
        ship_position[0] = ship_position[0] - (waypoint_relative_position[0] * distance)
    if waypoint_current_direction[1] == 'W':
        ship_position[0] = ship_position[0] - (waypoint_relative_position[1] * distance)
    if waypoint_current_direction[0] == 'N':
        ship_position[1] = ship_position[1] + (waypoint_relative_position[0] * distance)
    if waypoint_current_direction[1] == 'N':
        ship_position[1] = ship_position[1] + (waypoint_relative_position[1] * distance)
    if waypoint_current_direction[0] == 'S':
        ship_position[1] = ship_position[1] - (waypoint_relative_position[0] * distance)
    if waypoint_current_direction[1] == 'S':
        ship_position[1] = ship_position[1] - (waypoint_relative_position[1] * distance)

    return


def move_waypoint(waypoint_relative_position, waypoint_current_direction, directive, distance):
    if directive == 'E':
        if waypoint_current_direction[0] == 'E':
            waypoint_relative_position[0] += distance
        if waypoint_current_direction[0] == 'W':
            waypoint_relative_position[0] -= distance
        if waypoint_current_direction[1] == 'E':
            waypoint_relative_position[1] += distance
        if waypoint_current_direction[1] == 'W':
            waypoint_relative_position[1] -= distance
    elif directive == 'W':
        if waypoint_current_direction[0] == 'E':
            waypoint_relative_position[0] -= distance
        if waypoint_current_direction[0] == 'W':
            waypoint_relative_position[0] += distance
        if waypoint_current_direction[1] == 'E':
            waypoint_relative_position[1] -= distance
        if waypoint_current_direction[1] == 'W':
            waypoint_relative_position[1] += distance
    elif directive == 'N':
        if waypoint_current_direction[0] == 'N':
            waypoint_relative_position[0] += distance
        if waypoint_current_direction[0] == 'S':
            waypoint_relative_position[0] -= distance
        if waypoint_current_direction[1] == 'N':
            waypoint_relative_position[1] += distance
        if waypoint_current_direction[1] == 'S':
            waypoint_relative_position[1] -= distance
    elif directive == 'S':
        if waypoint_current_direction[0] == 'N':
            waypoint_relative_position[0] -= distance
        if waypoint_current_direction[0] == 'S':
            waypoint_relative_position[0] += distance
        if waypoint_current_direction[1] == 'N':
            waypoint_relative_position[1] -= distance
        if waypoint_current_direction[1] == 'S':
            waypoint_relative_position[1] += distance
    return


def part2():
    ship_position = [0, 0]
    waypoint_relative_position = [10, 1]
    waypoint_current_direction = ['E', 'N']
    for idx, instruction in enumerate(instructions):
        directive, distance = [instruction[0], int(instruction[1:])]
        if directive in ['R', 'L']:
            rotate_waypoint(waypoint_current_direction, directive, distance)
        elif directive == 'F':
            advance_ship(ship_position, waypoint_relative_position, waypoint_current_direction, distance)
        else:
            move_waypoint(waypoint_relative_position, waypoint_current_direction, directive, distance)

    print(f'manhattan distance: {abs(ship_position[0]) + abs(ship_position[1])}')
    return


if __name__ == "__main__":
    # part1()
    # 1294
    part2()
    # 20592
