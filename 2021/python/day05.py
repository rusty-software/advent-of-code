import time

with open("../input/day05.txt", "r") as fp:
    lines = [line.rstrip() for line in fp.readlines()]


def string_to_point(string_point):
    """
    Given a string point, returns a list of integers representing the point in the form [x, y].
    """
    return [int(x) for x in string_point.split(',')]


def endpoints_to_points(var_start, var_end, const_idx, const_idx_val):
    """
    Given a start value, end value, constant index, and constant value, returns a list of all integer points between
    the start and end.
    """
    line = []
    rs = min([var_start, var_end])
    re = max([var_start, var_end])
    for z in range(rs, re + 1):
        if const_idx == 0:
            line.append([const_idx_val, z])
        else:
            line.append([z, const_idx_val])

    return line


def endpoints_to_diagonal(start, end):
    """
    Given a start and end point, returns a list of all integer points between them. Assumes a 45 degree diagonal.
    """
    start_point = min(start, end)
    end_point = max(start, end)
    x_range = end_point[0] - start_point[0]
    y_incrementing = end_point[1] > start_point[1]
    points = []
    for x in range(x_range):
        if y_incrementing:
            points.append([start_point[0] + x, start_point[1] + x])
        else:
            points.append([start_point[0] + x, start_point[1] - x])

    points.append(end_point)
    return points


def line_to_points(unparsed_data, include_diagonals=False):
    """
    Given unparsed data, parses the data and returns the list of integer points between the start and end of the points
    defining the line. Only processes horizontal and vertical lines by default, and can return None.
    """
    start, end = unparsed_data.split(' -> ')
    start = string_to_point(start)
    end = string_to_point(end)
    if start[0] == end[0]:
        return endpoints_to_points(start[1], end[1], 0, start[0])
    elif start[1] == end[1]:
        return endpoints_to_points(start[0], end[0], 1, start[1])
    elif include_diagonals:
        return endpoints_to_diagonal(start, end)

    return None


def increment_touches(point_touches, points):
    """
    Given a dictionary of points to touch counts and a list of points, adds the point touches to the dictionary.
    """
    for p in points:
        point = tuple(p)
        if point in point_touches:
            point_touches[point] += 1
        else:
            point_touches[point] = 1

    return


def count_gte_touches(point_touches, threshold):
    """
    Given a dictionary of points to touch counts and a threshold, counts the number of points greater than or equal
    to the threshold.
    """
    keep_count = 0
    for k, v in point_touches.items():
        if v >= threshold:
            keep_count += 1

    return keep_count


def part1(include_diagonals=False):
    point_touches = dict()
    for line in lines:
        points = line_to_points(line, include_diagonals)
        if points:
            increment_touches(point_touches, points)

    overlaps = count_gte_touches(point_touches, 2)
    print(f'overlaps: {overlaps}')
    return


def part2():
    part1(True)
    return


def with_perf_timing(fn):
    start_time = time.perf_counter()
    fn()
    end_time = time.perf_counter()
    print(f'Execution time: {end_time - start_time:0.6f}')


if __name__ == "__main__":
    with_perf_timing(part1)
    # 7269

    with_perf_timing(part2)
    # 21140
